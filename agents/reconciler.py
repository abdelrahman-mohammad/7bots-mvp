import difflib
import itertools
import sys

from agents.element_check import as_is_dir, layer_dir
from agents.relationship_check import LAYERS, load_elements

THRESHOLD = 0.80


def normalize(name):
    cleaned = ""
    for character in name.lower():
        if character.isalnum():
            cleaned += character
    return cleaned


def similarity(first, second):
    return difflib.SequenceMatcher(None, first, second).ratio()


def merge_group(group):
    survivor = group[0]
    for other in group[1:]:
        for evidence in other.evidence:
            if evidence not in survivor.evidence:
                survivor.evidence.append(evidence)
        for relationship in other.relationships:
            if relationship not in survivor.relationships:
                survivor.relationships.append(relationship)
    return survivor


def find_conflicts(elements):
    conflicts = []
    for one, two in itertools.combinations(elements, 2):
        first = normalize(one.name)
        second = normalize(two.name)
        if first == second:
            conflicts.append(
                f"{one.id} ({one.layer}/{one.archimate_type}) and {two.id} ({two.layer}/{two.archimate_type}) share a name but differ in layer or type"
            )
        elif similarity(first, second) >= THRESHOLD:
            conflicts.append(
                f"{one.id} and {two.id} have similar names, {similarity(first, second):.2f}"
            )
    return conflicts


def reconcile(elements):
    groups = {}
    for element in sorted(elements, key=lambda item: item.id):
        key = (normalize(element.name), element.layer, element.archimate_type)
        groups.setdefault(key, []).append(element)

    merged = []
    for key in sorted(groups):
        merged.append(merge_group(groups[key]))

    return merged, find_conflicts(merged)


def main(system_id):
    elements = load_elements(system_id)
    merged, conflicts = reconcile(elements)

    for layer in LAYERS:
        for path in layer_dir(system_id, layer).glob("*.json"):
            path.unlink()

    for element in merged:
        path = layer_dir(system_id, element.layer) / f"{element.id}.json"
        path.write_text(element.model_dump_json(indent=2), encoding="utf-8")

    lines = ["# Reconciliation conflicts", ""]
    for conflict in conflicts:
        lines.append(f"- {conflict}")
    (as_is_dir(system_id) / "conflicts.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(
        f"{len(elements)} elements in, {len(merged)} after merge, {len(conflicts)} conflicts flagged"
    )
    for conflict in conflicts:
        print(f"  {conflict}")


if __name__ == "__main__":
    main(sys.argv[1])
