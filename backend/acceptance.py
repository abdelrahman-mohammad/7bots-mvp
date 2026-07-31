import json
import sys

from agents.element_check import grounding_error
from agents.schema import ModelElement
from backend.db import create_session
from backend.model_repo import git
from backend.repository.artifact_versions import list_artifact_versions
from backend.repository.elements import list_elements
from backend.repository.jobs import list_jobs

LAYERS = ["motivation", "strategy", "business", "application", "technology"]


def elements_on_main(system_id):
    listing = git("ls-tree", "-r", "--name-only", "origin/main", f"systems/{system_id}/as-is/")
    found = {}
    for path in listing.splitlines():
        if path.endswith(".json"):
            found[path] = json.loads(git("show", f"origin/main:{path}"))
    return found


def check(label, passed, detail):
    print(f"  [{'x' if passed else ' '}] {label}: {detail}")
    return passed


def main(system_id):
    git("fetch", "origin", "main")
    on_main = elements_on_main(system_id)
    session = create_session()
    results = []

    print("\nMerged model on the main branch")
    counts = {}
    for element in on_main.values():
        counts[element["layer"]] = counts.get(element["layer"], 0) + 1
    missing = [layer for layer in LAYERS if not counts.get(layer)]
    results.append(
        check(
            "all five layers produced",
            not missing,
            ", ".join(f"{layer} {counts.get(layer, 0)}" for layer in LAYERS),
        )
    )

    invalid = []
    ungrounded = []
    for path, data in on_main.items():
        try:
            element = ModelElement(**data)
        except Exception as error:
            invalid.append(f"{path}: {error}")
            continue
        reason = grounding_error(element.evidence)
        if reason:
            ungrounded.append(f"{element.id}: {reason}")

    results.append(check("every element schema-valid", not invalid, f"{len(on_main)} checked"))
    results.append(
        check(
            "every element grounded in real evidence", not ungrounded, f"{len(ungrounded)} failed"
        )
    )

    print("\nAssembly artifacts committed alongside the model")
    for name in ["conflicts.md", "validation-report.md"]:
        try:
            body = git("show", f"origin/main:systems/{system_id}/as-is/{name}")
            results.append(check(name, True, f"{len(body.splitlines())} lines"))
        except RuntimeError:
            results.append(check(name, False, "missing"))

    print("\nApproval and database state")
    versions = list_artifact_versions(session, system_id)
    approved = [v for v in versions if v.approval_status == "approved" and v.tag]
    results.append(
        check(
            "an artifact version is approved and linked to a PR",
            bool(approved),
            ", ".join(f"{v.tag} {v.commit_sha[:8]}" for v in approved) or "none",
        )
    )

    indexed = {element.git_path for element in list_elements(session, system_id)}
    results.append(
        check(
            "index matches the merged model exactly",
            indexed == set(on_main),
            f"{len(indexed)} indexed against {len(on_main)} on main",
        )
    )

    traced = [job for job in list_jobs(session, system_id) if job.run_id]
    results.append(
        check(
            "a completed job carries a LangSmith run id",
            bool(traced),
            traced[-1].run_id if traced else "none",
        )
    )

    session.close()
    print(f"\n{sum(results)} of {len(results)} automated checks passed")
    if not all(results):
        sys.exit(1)


if __name__ == "__main__":
    main(sys.argv[1])
