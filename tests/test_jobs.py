from fastapi.testclient import TestClient

from backend import api, jobs
from backend.db import create_session
from backend.repository.jobs import get_job

client = TestClient(api.app)


def status_of(job_id):
    session = create_session()
    try:
        return get_job(session, job_id)
    finally:
        session.close()


def test_trigger_returns_a_job_id_immediately(monkeypatch):
    monkeypatch.setattr(api, "run_job", lambda *args: None)
    response = client.post("/systems/shiptrack/ingest")
    assert response.status_code == 200
    assert response.json()["status"] == "queued"
    assert isinstance(response.json()["job_id"], int)


def test_successful_run_ends_in_succeeded(monkeypatch):
    monkeypatch.setattr(jobs, "run_as_is_ingestion", lambda system_id, evidence_path: None)
    job_id = client.post("/systems/shiptrack/ingest").json()["job_id"]

    jobs.run_job(job_id, "shiptrack", "./test-fixtures/evidence")

    job = status_of(job_id)
    assert job.status == "succeeded"
    assert job.started_at is not None
    assert job.finished_at is not None


def test_crash_ends_in_failed_with_an_error_message(monkeypatch):
    def boom(system_id, evidence_path):
        raise RuntimeError("validation found 3 violations, not committing")

    monkeypatch.setattr(jobs, "run_as_is_ingestion", boom)
    job_id = client.post("/systems/shiptrack/ingest").json()["job_id"]

    jobs.run_job(job_id, "shiptrack", "./test-fixtures/evidence")

    job = status_of(job_id)
    assert job.status == "failed"
    assert "validation found 3 violations" in job.error_message
    assert job.finished_at is not None
