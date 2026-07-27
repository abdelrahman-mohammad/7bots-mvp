import json
import sys

from pydantic import ValidationError

from agents.element_check import as_is_dir, layer_dir
from agents.relationship_check import LAYERS
from agents.schema import ELEMENT_TYPES, SKILL, ModelElement

MATRIX_FILE = SKILL.parent / "references" / "relationships.md"


def load_matrix():
    matrix = {}
    for line in MATRIX_FILE.read_text(encoding="utf-8").splitlines():
        if " -> " not in line or ":" not in line:
            continue
        pair, _, types = line.partition(":")
        source, _, target = pair.partition(" -> ")
        if source.strip() not in ELEMENT_TYPES:
            continue
        allowed = []
        for name in types.split(","):
            allowed.append(name.strip())
        matrix[(source.strip(), target.strip())] = allowed
    return matrix


MATRIX = load_matrix()


def check(raw_elements):
    elements = []
    problems = []

    for name, data in raw_elements:
        try:
            elements.append(ModelElement(**data))
        except ValidationError as error:
            problems.append(f"{name}: {error.errors()[0]['msg']}")

    by_id = {}
    for element in elements:
        by_id[element.id] = element

    for element in elements:
        for relationship in element.relationships:
            target = by_id.get(relationship.target_id)
            if target is None:
                problems.append(
                    f"{element.id}: relationship points at unknown id {relationship.target_id}"
                )
                continue
            allowed = MATRIX.get((element.archimate_type, target.archimate_type), [])
            if relationship.type not in allowed:
                problems.append(
                    f"{element.id}: {relationship.type} from {element.archimate_type} to {target.archimate_type} is not permitted"
                )

    return elements, problems


def build_report(elements, problems):
    counts = {}
    for element in elements:
        counts[element.layer] = counts.get(element.layer, 0) + 1

    lines = ["# Validation report", "", f"{len(elements)} elements", ""]
    for layer in LAYERS:
        lines.append(f"- {layer}: {counts.get(layer, 0)}")
    lines.append("")

    if problems:
        lines.append(f"## {len(problems)} violations")
        lines.append("")
        for problem in problems:
            lines.append(f"- {problem}")
    else:
        lines.append("No violations found.")

    return "\n".join(lines) + "\n"


def main():
    raw_elements = []
    for layer in LAYERS:
        for path in sorted(layer_dir(layer).glob("*.json")):
            raw_elements.append((path.name, json.loads(path.read_text(encoding="utf-8"))))

    elements, problems = check(raw_elements)
    report = build_report(elements, problems)

    (as_is_dir() / "validation-report.md").write_text(report, encoding="utf-8")
    print(report)

    if problems:
        sys.exit(1)


if __name__ == "__main__":
    main()
