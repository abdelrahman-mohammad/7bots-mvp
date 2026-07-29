import os
import shutil
import sys
from datetime import UTC, datetime

from agents import reconciler
from agents.agent import create_agent
from agents.element_check import layer_dir
from agents.validator import validate
from backend.model_repo import commit_to_model, open_pull_request

EXTRACTORS = {
    "strategy-analyst": ["motivation", "strategy"],
    "business-analyst": ["business"],
    "code-analyzer": ["application"],
    "infra-analyzer": ["technology"],
}


def dispatch(task):
    create_agent().invoke({"messages": [{"role": "user", "content": task}]})


def extract(system_id):
    for layers in EXTRACTORS.values():
        for layer in layers:
            shutil.rmtree(layer_dir(system_id, layer), ignore_errors=True)
            layer_dir(system_id, layer).mkdir(parents=True)

    names = ", ".join(EXTRACTORS)
    dispatch(
        f"Extract elements for system id {system_id}. Use the task tool to call all of these"
        f" subagents in parallel: {names}. Each one follows its own system prompt."
    )


def map_integrations(system_id):
    dispatch(
        f"Use the task tool to call integration-mapper. Give it this task: add relationships"
        f" for system id {system_id}, following your system prompt."
    )


def run_as_is_ingestion(system_id, evidence_path):
    os.environ["EVIDENCE_PATH"] = evidence_path
    run_id = "run-" + datetime.now(UTC).strftime("%Y%m%d-%H%M%S")

    extract(system_id)
    map_integrations(system_id)
    reconciler.main(system_id)

    report, problems = validate(system_id)
    print(report)
    if problems:
        raise RuntimeError(f"validation found {len(problems)} violations, not committing")

    branch = commit_to_model(system_id, run_id)
    number = open_pull_request(system_id, run_id)
    return {"run_id": run_id, "branch": branch, "pull_request": number}


if __name__ == "__main__":
    print(run_as_is_ingestion(sys.argv[1], sys.argv[2]))
