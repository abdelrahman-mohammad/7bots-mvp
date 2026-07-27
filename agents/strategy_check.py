import shutil
from pathlib import Path

from pydantic import ValidationError

from agents.agent import create_agent
from agents.schema import ModelElement
from backend.config import require

SYSTEM_ID = "shiptrack"
LAYERS = ["motivation", "strategy"]
TASK = f"Use the task tool to call strategy-analyst. The system id is {SYSTEM_ID}."


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


def run():
    (as_is_dir() / "rejected.md").unlink(missing_ok=True)
    for layer in LAYERS:
        shutil.rmtree(layer_dir(layer), ignore_errors=True)
        layer_dir(layer).mkdir(parents=True)

    create_agent().invoke({"messages": [{"role": "user", "content": TASK}]})

    total = 0
    for layer in LAYERS:
        files = sorted(layer_dir(layer).glob("*.json"))
        print(f"\n{layer}: {len(files)} elements")
        for path in files:
            print("  " + check_element(path))
        total += len(files)
    return total


if __name__ == "__main__":
    print("=== run 1 ===")
    first = run()
    print("\n=== run 2 ===")
    second = run()
    print(f"\nrun 1: {first} elements, run 2: {second}, difference {abs(first - second)}")
