from fastapi.testclient import TestClient

from backend import api
from backend.config import require

client = TestClient(api.app)
AUTH = {"X-API-Key": require("API_KEY")}


def test_request_without_an_api_key_is_rejected():
    assert client.get("/systems/shiptrack/elements").status_code == 401


def test_request_with_a_wrong_api_key_is_rejected():
    response = client.get("/systems/shiptrack/elements", headers={"X-API-Key": "wrong"})
    assert response.status_code == 401


def test_all_five_endpoints_are_in_the_openapi_schema():
    paths = client.get("/openapi.json").json()["paths"]
    assert "/systems/{system_id}/ingest" in paths
    assert "/jobs/{job_id}" in paths
    assert "/systems/{system_id}/elements" in paths
    assert "/elements/{element_id}" in paths
    assert "/systems/{system_id}/artifact-versions" in paths


def test_job_status_is_readable(monkeypatch):
    monkeypatch.setattr(api, "run_job", lambda *args: None)
    job_id = client.post("/systems/shiptrack/ingest", headers=AUTH).json()["job_id"]

    response = client.get(f"/jobs/{job_id}", headers=AUTH)
    assert response.status_code == 200
    assert response.json()["status"] == "queued"


def test_unknown_job_is_404():
    assert client.get("/jobs/99999999", headers=AUTH).status_code == 404


def test_elements_can_be_filtered_by_layer():
    everything = client.get("/systems/shiptrack/elements", headers=AUTH).json()
    business = client.get("/systems/shiptrack/elements?layer=business", headers=AUTH).json()
    assert len(business) <= len(everything)
    assert all(element["layer"] == "business" for element in business)


def test_element_detail_reads_evidence_from_the_repo():
    listed = client.get("/systems/shiptrack/elements?layer=business", headers=AUTH).json()
    response = client.get(f"/elements/{listed[0]['id']}", headers=AUTH)
    assert response.status_code == 200
    assert response.json()["evidence"]


def test_unknown_element_is_404():
    assert client.get("/elements/no-such-element", headers=AUTH).status_code == 404


def test_artifact_versions_are_listed():
    response = client.get("/systems/shiptrack/artifact-versions", headers=AUTH)
    assert response.status_code == 200
    assert response.json()[0]["approval_status"] in ("pending", "approved")
