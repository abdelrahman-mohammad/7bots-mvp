import pytest

from backend import orchestrator


def test_validation_failure_stops_before_commit(monkeypatch):
    reached = []

    monkeypatch.setattr(orchestrator, "extract", lambda system_id: None)
    monkeypatch.setattr(orchestrator, "map_integrations", lambda system_id: None)
    monkeypatch.setattr(orchestrator.reconciler, "main", lambda system_id: None)
    monkeypatch.setattr(orchestrator, "validate", lambda system_id: ("report", ["bad type"]))
    monkeypatch.setattr(orchestrator, "commit_to_model", lambda *args: reached.append("G1"))
    monkeypatch.setattr(orchestrator, "open_pull_request", lambda *args: reached.append("G2"))

    with pytest.raises(RuntimeError, match="validation found 1 violations"):
        orchestrator.run_as_is_ingestion("shiptrack", "./test-fixtures/evidence")

    assert reached == []
