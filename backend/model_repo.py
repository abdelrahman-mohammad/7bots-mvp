import json
import shutil
import subprocess
import sys
import urllib.error
import urllib.request
from datetime import UTC, datetime
from pathlib import Path

from backend.config import require
from backend.db import create_session
from backend.repository.artifact_versions import create_artifact_version

GIT = shutil.which("git") or "git"


def scrub(text):
    return text.replace(require("GITHUB_TOKEN"), "***")


def git(*args):
    result = subprocess.run(
        [GIT, "-C", require("MODEL_REPO_PATH"), *args],
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        raise RuntimeError(scrub(result.stderr.strip()))
    return result.stdout.strip()


def branch_name(system_id, run_id):
    return f"feature/ingest-{system_id}-{run_id}"


def branch_exists(branch):
    return git("branch", "--list", branch) != ""


def push(branch):
    url = f"https://x-access-token:{require('GITHUB_TOKEN')}@github.com/{require('GITHUB_MODEL_REPO')}.git"
    git("push", url, branch)


def commit_to_model(system_id, run_id):
    branch = branch_name(system_id, run_id)
    if branch_exists(branch):
        return branch

    git("checkout", "-b", branch)
    git("add", "-A")
    git("commit", "-m", f"feat: ingest {system_id} as-is model (run {run_id})")
    push(branch)
    return branch


def as_is_dir(system_id):
    return Path(require("MODEL_REPO_PATH")) / "systems" / system_id / "as-is"


def pull_request_body(system_id, run_id):
    stamp = datetime.now(UTC).isoformat(timespec="seconds")
    parts = [f"Run `{run_id}` for `{system_id}` at {stamp}."]
    for name in ["validation-report.md", "conflicts.md"]:
        report = as_is_dir(system_id) / name
        if report.exists():
            parts.append(report.read_text(encoding="utf-8").strip())
    return "\n\n".join(parts)


def post_pull_request(branch, title, body):
    payload = {"title": title, "head": branch, "base": "main", "body": body}
    request = urllib.request.Request(
        f"https://api.github.com/repos/{require('GITHUB_MODEL_REPO')}/pulls",
        data=json.dumps(payload).encode(),
        headers={
            "Authorization": f"Bearer {require('GITHUB_TOKEN')}",
            "Accept": "application/vnd.github+json",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(request) as response:
            return json.load(response)["number"]
    except urllib.error.HTTPError as error:
        raise RuntimeError(scrub(error.read().decode())) from error


def open_pull_request(system_id, run_id):
    branch = branch_name(system_id, run_id)
    title = f"Ingest {system_id} as-is model (run {run_id})"
    number = post_pull_request(branch, title, pull_request_body(system_id, run_id))

    session = create_session()
    try:
        create_artifact_version(
            session,
            system_id=system_id,
            commit_sha=git("rev-parse", branch),
            phase="1",
            author_type="agent",
            tag=f"pr-{number}",
            run_id=run_id,
        )
        session.commit()
    finally:
        session.close()

    return number


if __name__ == "__main__":
    action, system_id, run_id = sys.argv[1], sys.argv[2], sys.argv[3]
    if action == "commit":
        print(commit_to_model(system_id, run_id))
    else:
        print(open_pull_request(system_id, run_id))
