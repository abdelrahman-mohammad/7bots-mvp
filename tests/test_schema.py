import pytest
from pydantic import ValidationError

from agents.schema import ModelElement


def element(**overrides):
    data = {
        "id": "app-payment-service",
        "layer": "application",
        "archimate_type": "ApplicationComponent",
        "name": "Payment Service",
        "documentation": "Handles card payments.",
        "confidence": "observed",
        "evidence": [
            {
                "source_type": "code",
                "locator": "src/payments/service.py:1-40",
                "excerpt": "class PaymentService:",
            }
        ],
    }
    data.update(overrides)
    return data


def test_valid_element():
    parsed = ModelElement(**element())
    assert parsed.archimate_type == "ApplicationComponent"


def test_empty_evidence_fails():
    with pytest.raises(ValidationError):
        ModelElement(**element(evidence=[]))


def test_unknown_archimate_type_fails():
    with pytest.raises(ValidationError):
        ModelElement(**element(archimate_type="BusinessComponent"))


def test_unknown_relationship_type_fails():
    relationships = [{"target_id": "data-claim-record", "type": "Consumes"}]
    with pytest.raises(ValidationError):
        ModelElement(**element(relationships=relationships))


def test_valid_relationship_is_accepted():
    relationships = [{"target_id": "data-claim-record", "type": "Access"}]
    parsed = ModelElement(**element(relationships=relationships))
    assert parsed.relationships[0].type == "Access"
