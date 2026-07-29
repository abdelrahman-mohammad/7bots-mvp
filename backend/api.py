import hashlib
import hmac
import json

from fastapi import FastAPI, Header, HTTPException, Request

from backend.config import require
from backend.db import create_session
from backend.model_repo import git
from backend.repository.artifact_versions import get_artifact_version, set_approval
from backend.repository.elements import upsert_element

app = FastAPI()


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
        if version.approval_status == "approved":  # type: ignore
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
