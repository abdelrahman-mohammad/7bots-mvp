import sys

from pydantic import ValidationError

from agents.agent import create_agent
from agents.element_check import as_is_dir, grounding_error, layer_dir
from agents.schema import ModelElement

LAYERS = ["motivation", "strategy", "business", "application", "technology"]


def load_elements(system_id):
    elements = []
    for layer in LAYERS:
        for path in sorted(layer_dir(system_id, layer).glob("*.json")):
            try:
                elements.append(ModelElement.model_validate_json(path.read_text(encoding="utf-8")))
            except ValidationError as error:
                print(f"  INVALID {path.name}: {error.errors()[0]['msg']}")
    return elements


def check_relationship(element, relationship, known_ids):
    if relationship.target_id not in known_ids:
        return f"BROKEN {element.id} -> {relationship.target_id}: no element has that id"

    reason = grounding_error(relationship.evidence)
    if reason:
        return f"UNGROUNDED {element.id} -> {relationship.target_id}: {reason}"

    return f"ok {element.id} -{relationship.type}-> {relationship.target_id}"


def report(system_id):
    elements = load_elements(system_id)
    known_ids = {element.id for element in elements}
    print(f"\n{len(elements)} elements in the model")

    total = 0
    for element in elements:
        for relationship in element.relationships:
            print("  " + check_relationship(element, relationship, known_ids))
            total += 1
    print(f"\n{total} relationships")

    rejected = as_is_dir(system_id) / "rejected.md"
    if rejected.exists():
        print("\nrejected:")
        print(rejected.read_text(encoding="utf-8").strip())


def main(system_id):
    (as_is_dir(system_id) / "rejected.md").unlink(missing_ok=True)
    task = f"Use the task tool to call integration-mapper. Give it this task: add relationships for system id {system_id}, following your system prompt."
    create_agent().invoke({"messages": [{"role": "user", "content": task}]})
    report(system_id)


if __name__ == "__main__":
    main(sys.argv[1])
