import hashlib
import hmac
import json

from fastapi.testclient import TestClient

from backend.api import app

client = TestClient(app)
BODY = json.dumps({"action": "closed"}).encode()


def test_missing_signature_is_rejected():
    assert client.post("/webhooks/github", content=BODY).status_code == 401


def test_signature_from_a_different_secret_is_rejected():
    forged = "sha256=" + hmac.new(b"not-the-secret", BODY, hashlib.sha256).hexdigest()
    response = client.post(
        "/webhooks/github", content=BODY, headers={"X-Hub-Signature-256": forged}
    )
    assert response.status_code == 401
