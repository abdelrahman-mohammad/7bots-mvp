import shutil
import subprocess
import sys

from backend.config import require

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

    git("checkout", "-b", branch, "main")
    git("add", "-A")
    git("commit", "-m", f"feat: ingest {system_id} as-is model (run {run_id})")
    push(branch)
    return branch


if __name__ == "__main__":
    print(commit_to_model(sys.argv[1], sys.argv[2]))
