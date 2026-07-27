import shutil
import sys
from pathlib import Path

from pydantic import ValidationError

from agents.agent import create_agent
from agents.schema import ModelElement
from backend.config import require

SYSTEM_ID = "shiptrack"


def as_is_dir():
    return Path(require("MODEL_REPO_PATH")) / "systems" / SYSTEM_ID / "as-is"


def layer_dir(layer):
    return as_is_dir() / layer


def evidence_file(locator):
    relative = locator.replace("/evidence/", "", 1).lstrip("/")
    return Path(require("EVIDENCE_PATH")) / relative


def check_element(path):
    try:
        element = ModelElement.model_validate_json(path.read_text(encoding="utf-8"))
    except ValidationError as error:
        return f"INVALID {path.name}: {error.errors()[0]['msg']}"

    for evidence in element.evidence:
        source = evidence_file(evidence.locator)
        if not source.exists():
            return f"UNGROUNDED {path.name}: no such file {evidence.locator}"
        if evidence.excerpt not in source.read_text(encoding="utf-8"):
            return f"UNGROUNDED {path.name}: excerpt is not verbatim in {evidence.locator}"

    return f"ok {path.name}: {element.archimate_type} {element.name}"


def run(subagent, layers):
    (as_is_dir() / "rejected.md").unlink(missing_ok=True)
    for layer in layers:
        shutil.rmtree(layer_dir(layer), ignore_errors=True)
        layer_dir(layer).mkdir(parents=True)

    task = f"Use the task tool to call {subagent}. Give it this task: extract elements for system id {SYSTEM_ID}, following your system prompt."
    create_agent().invoke({"messages": [{"role": "user", "content": task}]})

    total = 0
    for layer in layers:
        files = sorted(layer_dir(layer).glob("*.json"))
        print(f"\n{layer}: {len(files)} elements")
        for path in files:
            print("  " + check_element(path))
        total += len(files)
    return total


if __name__ == "__main__":
    subagent = sys.argv[1]
    layers = sys.argv[2:]
    print("=== run 1 ===")
    first = run(subagent, layers)
    print("\n=== run 2 ===")
    second = run(subagent, layers)
    print(f"\nrun 1: {first} elements, run 2: {second}, difference {abs(first - second)}")
