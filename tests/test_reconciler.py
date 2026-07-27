from agents.reconciler import normalize, reconcile
from agents.schema import ModelElement


def element(element_id, name, layer="technology", archimate_type="Node", locator="main.tf:1"):
    return ModelElement(
        id=element_id,
        layer=layer,  # type: ignore
        archimate_type=archimate_type,
        name=name,
        documentation="A machine.",
        confidence="observed",
        evidence=[
            {
                "source_type": "document",
                "locator": f"/evidence/infra/{locator}",
                "excerpt": "shipdb-primary",
            }
        ],  # type: ignore
    )


def test_normalize_strips_case_and_punctuation():
    assert normalize("SHIPDB PRIMARY") == normalize("shipdb-primary")


def test_near_duplicates_merge_into_one():
    pair = [
        element("tf-shipdb", "shipdb-primary", locator="main.tf:5"),
        element("cmdb-shipdb", "SHIPDB PRIMARY", locator="cmdb-export.csv:2"),
    ]
    merged, conflicts = reconcile(pair)
    assert len(merged) == 1
    assert conflicts == []


def test_merged_element_keeps_evidence_from_both_sources():
    pair = [
        element("tf-shipdb", "shipdb-primary", locator="main.tf:5"),
        element("cmdb-shipdb", "SHIPDB PRIMARY", locator="cmdb-export.csv:2"),
    ]
    merged, _ = reconcile(pair)
    locators = sorted(evidence.locator for evidence in merged[0].evidence)
    assert locators == ["/evidence/infra/cmdb-export.csv:2", "/evidence/infra/main.tf:5"]


def test_same_name_in_different_layers_is_flagged_not_merged():
    pair = [
        element("res-dispatch-team", "Dispatch team", layer="strategy", archimate_type="Resource"),
        element(
            "act-dispatch-team", "Dispatch Team", layer="business", archimate_type="BusinessActor"
        ),
    ]
    merged, conflicts = reconcile(pair)
    assert len(merged) == 2
    assert len(conflicts) == 1


def test_similar_but_not_equal_names_are_flagged_not_merged():
    pair = [
        element("payment-service", "Payment Service"),
        element("payment-svc", "PaymentSvc"),
    ]
    merged, conflicts = reconcile(pair)
    assert len(merged) == 2
    assert len(conflicts) == 1


def test_unrelated_names_are_left_alone():
    pair = [
        element("customer", "Customer"),
        element("consignment", "Consignment"),
    ]
    merged, conflicts = reconcile(pair)
    assert len(merged) == 2
    assert conflicts == []


def test_reconcile_is_deterministic_regardless_of_input_order():
    first = element("tf-shipdb", "shipdb-primary", locator="main.tf:5")
    second = element("cmdb-shipdb", "SHIPDB PRIMARY", locator="cmdb-export.csv:2")
    third = element("scanner", "Depot Scanner Fleet", archimate_type="Device")

    forward, _ = reconcile([first, second, third])
    backward, _ = reconcile([third, second, first])
    assert [item.id for item in forward] == [item.id for item in backward]
