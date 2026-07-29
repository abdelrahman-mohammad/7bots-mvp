import hashlib
import hmac
import json

from fastapi import APIRouter, BackgroundTasks, Depends, FastAPI, Header, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware

from backend.config import require
from backend.db import create_session
from backend.jobs import run_job
from backend.model_repo import git
from backend.repository.artifact_versions import (
    get_artifact_version,
    list_artifact_versions,
    set_approval,
)
from backend.repository.elements import get_element, list_elements, upsert_element
from backend.repository.jobs import create_job, get_job

app = FastAPI(title="7bots Phase 1 API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[require("FRONTEND_ORIGIN")],
    allow_methods=["*"],
    allow_headers=["*"],
)


def session_scope():
    session = create_session()
    try:
        yield session
    finally:
        session.close()


def require_api_key(x_api_key: str = Header(default="")):
    if not hmac.compare_digest(x_api_key, require("API_KEY")):
        raise HTTPException(status_code=401, detail="invalid api key")


api = APIRouter(dependencies=[Depends(require_api_key)])


def element_summary(element):
    return {
        "id": element.id,
        "layer": element.layer,
        "archimate_type": element.archimate_type,
        "name": element.name,
        "git_path": element.git_path,
        "current_commit": element.current_commit,
    }


@api.post("/systems/{system_id}/ingest")
def trigger_ingestion(system_id: str, background: BackgroundTasks, session=Depends(session_scope)):
    job = create_job(session, system_id, phase="1")
    session.commit()
    background.add_task(run_job, job.id, system_id, require("EVIDENCE_PATH"))
    return {"job_id": job.id, "status": "queued"}


@api.get("/jobs/{job_id}")
def read_job(job_id: int, session=Depends(session_scope)):
    job = get_job(session, job_id)
    if job is None:
        raise HTTPException(status_code=404, detail="no such job")
    return {
        "id": job.id,
        "system_id": job.system_id,
        "status": job.status,
        "run_id": job.run_id,
        "error_message": job.error_message,
        "started_at": job.started_at,
        "finished_at": job.finished_at,
    }


@api.get("/systems/{system_id}/elements")
def read_elements(system_id: str, layer: str | None = None, session=Depends(session_scope)):
    return [element_summary(element) for element in list_elements(session, system_id, layer)]


@api.get("/elements/{element_id}")
def read_element(element_id: str, session=Depends(session_scope)):
    element = get_element(session, element_id)
    if element is None:
        raise HTTPException(status_code=404, detail="no such element")
    try:
        return json.loads(git("show", f"origin/main:{element.git_path}"))
    except RuntimeError as error:
        raise HTTPException(status_code=404, detail="not on the main branch yet") from error


@api.get("/systems/{system_id}/artifact-versions")
def read_artifact_versions(system_id: str, session=Depends(session_scope)):
    versions = list_artifact_versions(session, system_id)
    return [
        {
            "commit_sha": version.commit_sha,
            "tag": version.tag,
            "run_id": version.run_id,
            "approval_status": version.approval_status,
            "approved_by": version.approved_by,
            "created_at": version.created_at,
        }
        for version in versions
    ]


app.include_router(api)


def signature_matches(body, signature):
    secret = require("GITHUB_WEBHOOK_SECRET").encode()
    expected = "sha256=" + hmac.new(secret, body, hashlib.sha256).hexdigest()
    return hmac.compare_digest(expected, signature)


def refresh_index(session, system_id, commit_sha):
    git("fetch", "origin", "main")
    listing = git("ls-tree", "-r", "--name-only", "origin/main", f"systems/{system_id}/as-is/")
    for path in listing.splitlines():
        if not path.endswith(".json"):
            continue
        element = json.loads(git("show", f"origin/main:{path}"))
        upsert_element(
            session,
            element_id=element["id"],
            system_id=system_id,
            layer=element["layer"],
            archimate_type=element["archimate_type"],
            name=element["name"],
            git_path=path,
            current_commit=commit_sha,
        )


def approve(head_sha, merge_sha):
    session = create_session()
    try:
        version = get_artifact_version(session, head_sha)
        if version is None:
            raise HTTPException(status_code=404, detail="no artifact version for that commit")
        if version.approval_status == "approved":
            return {"status": "already approved"}

        set_approval(session, head_sha, "approved")
        refresh_index(session, version.system_id, merge_sha)
        session.commit()
        return {"status": "approved"}
    finally:
        session.close()


@app.post("/webhooks/github")
async def github_webhook(request: Request, x_hub_signature_256: str = Header(default="")):
    body = await request.body()
    if not signature_matches(body, x_hub_signature_256):
        raise HTTPException(status_code=401, detail="invalid signature")

    event = json.loads(body)
    pull_request = event.get("pull_request", {})
    if event.get("action") != "closed" or not pull_request.get("merged"):
        return {"status": "ignored"}

    return approve(pull_request["head"]["sha"], pull_request["merge_commit_sha"])
