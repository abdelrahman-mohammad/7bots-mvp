from pydantic import ValidationError

from agents.agent import create_agent
from agents.element_check import SYSTEM_ID, as_is_dir, grounding_error, layer_dir
from agents.schema import ModelElement

LAYERS = ["motivation", "strategy", "business", "application", "technology"]
TASK = f"Use the task tool to call integration-mapper. Give it this task: add relationships for system id {SYSTEM_ID}, following your system prompt."


def load_elements():
    elements = []
    for layer in LAYERS:
        for path in sorted(layer_dir(layer).glob("*.json")):
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


def report():
    elements = load_elements()
    known_ids = {element.id for element in elements}
    print(f"\n{len(elements)} elements in the model")

    total = 0
    for element in elements:
        for relationship in element.relationships:
            print("  " + check_relationship(element, relationship, known_ids))
            total += 1
    print(f"\n{total} relationships")

    rejected = as_is_dir() / "rejected.md"
    if rejected.exists():
        print("\nrejected:")
        print(rejected.read_text(encoding="utf-8").strip())


def main():
    (as_is_dir() / "rejected.md").unlink(missing_ok=True)
    create_agent().invoke({"messages": [{"role": "user", "content": TASK}]})
    report()


if __name__ == "__main__":
    main()
