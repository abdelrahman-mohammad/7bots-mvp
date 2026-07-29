import shutil
import sys
from pathlib import Path

from pydantic import ValidationError

from agents.agent import create_agent
from agents.schema import ModelElement
from backend.config import require


def as_is_dir(system_id):
    return Path(require("MODEL_REPO_PATH")) / "systems" / system_id / "as-is"


def layer_dir(system_id, layer):
    return as_is_dir(system_id) / layer


def evidence_file(locator):
    relative = locator.split(":")[0].replace("/evidence/", "", 1).lstrip("/")
    return Path(require("EVIDENCE_PATH")) / relative


def cited_text(source, locator):
    text = source.read_text(encoding="utf-8")
    if ":" not in locator:
        return text

    first, _, last = locator.split(":")[1].partition("-")
    if not first.isdigit():
        return ""
    end = int(last) if last.isdigit() else int(first)
    return "\n".join(text.splitlines()[int(first) - 1 : end])


def grounding_error(evidence_list):
    for evidence in evidence_list:
        source = evidence_file(evidence.locator)
        if not source.exists():
            return f"no such file {evidence.locator}"
        if evidence.excerpt not in cited_text(source, evidence.locator):
            return f"excerpt is not verbatim at {evidence.locator}"
    return None


def check_element(path):
    try:
        element = ModelElement.model_validate_json(path.read_text(encoding="utf-8"))
    except ValidationError as error:
        return f"INVALID {path.name}: {error.errors()[0]['msg']}"

    reason = grounding_error(element.evidence)
    if reason:
        return f"UNGROUNDED {path.name}: {reason}"

    return f"ok {path.name}: {element.archimate_type} {element.name}"


def run(system_id, subagent, layers):
    (as_is_dir(system_id) / "rejected.md").unlink(missing_ok=True)
    (as_is_dir(system_id) / "files-read.md").unlink(missing_ok=True)
    for layer in layers:
        shutil.rmtree(layer_dir(system_id, layer), ignore_errors=True)
        layer_dir(system_id, layer).mkdir(parents=True)

    task = f"Use the task tool to call {subagent}. Give it this task: extract elements for system id {system_id}, following your system prompt."
    create_agent().invoke({"messages": [{"role": "user", "content": task}]})

    total = 0
    for layer in layers:
        files = sorted(layer_dir(system_id, layer).glob("*.json"))
        print(f"\n{layer}: {len(files)} elements")
        for path in files:
            print("  " + check_element(path))
        total += len(files)

    read_log = as_is_dir(system_id) / "files-read.md"
    if read_log.exists():
        print("\nfiles read:")
        print(read_log.read_text(encoding="utf-8").strip())
    return total


if __name__ == "__main__":
    system_id, subagent = sys.argv[1], sys.argv[2]
    layers = sys.argv[3:]
    print("=== run 1 ===")
    first = run(system_id, subagent, layers)
    print("\n=== run 2 ===")
    second = run(system_id, subagent, layers)
    print(f"\nrun 1: {first} elements, run 2: {second}, difference {abs(first - second)}")
