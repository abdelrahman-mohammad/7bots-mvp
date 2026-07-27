from agents.validator import MATRIX, check


def raw(element_id, archimate_type, layer, relationships=None):
    return (
        f"{element_id}.json",
        {
            "id": element_id,
            "layer": layer,
            "archimate_type": archimate_type,
            "name": element_id,
            "documentation": "Something.",
            "confidence": "observed",
            "evidence": [
                {
                    "source_type": "document",
                    "locator": "/evidence/code/schema.sql:3",
                    "excerpt": "CREATE TABLE customer (",
                }
            ],
            "relationships": relationships or [],
        },
    )


def relationship(target_id, relationship_type):
    return {
        "target_id": target_id,
        "type": relationship_type,
        "evidence": [
            {
                "source_type": "document",
                "locator": "/evidence/code/schema.sql:3",
                "excerpt": "CREATE TABLE customer (",
            }
        ],
    }


def test_matrix_loaded_from_the_skill():
    assert MATRIX[("ApplicationComponent", "DataObject")]
    assert ("BusinessProcess", "Node") in MATRIX


def test_clean_model_has_no_problems():
    elements, problems = check(
        [
            raw(
                "booking", "ApplicationComponent", "application", [relationship("claims", "Access")]
            ),
            raw("claims", "DataObject", "application"),
        ]
    )
    assert len(elements) == 2
    assert problems == []


def test_invalid_archimate_type_is_flagged():
    _, problems = check([raw("booking", "BusinessComponent", "business")])
    assert len(problems) == 1
    assert "booking.json" in problems[0]


def test_illegal_relationship_between_layers_is_flagged():
    _, problems = check(
        [
            raw("book", "BusinessProcess", "business", [relationship("host", "Realization")]),
            raw("host", "Node", "technology"),
        ]
    )
    assert len(problems) == 1
    assert "not permitted" in problems[0]


def test_missing_evidence_is_flagged():
    name, data = raw("booking", "ApplicationComponent", "application")
    data["evidence"] = []
    _, problems = check([(name, data)])
    assert len(problems) == 1


def test_relationship_to_unknown_id_is_flagged():
    _, problems = check(
        [raw("booking", "ApplicationComponent", "application", [relationship("invgw", "Flow")])]
    )
    assert len(problems) == 1
    assert "unknown id" in problems[0]
