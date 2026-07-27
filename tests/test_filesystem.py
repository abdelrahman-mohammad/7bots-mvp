from pathlib import Path

from agents.filesystem import create_backend
from backend.config import require


def test_evidence_can_be_read():
    result = create_backend().read("/evidence/infra/main.tf")
    assert result.error is None
    assert "shipdb-primary" in result.file_data["content"]  # type: ignore


def test_evidence_can_be_searched():
    result = create_backend().grep(pattern="consignment", path="/evidence")
    assert result.matches


def test_writing_to_evidence_is_refused():
    result = create_backend().write("/evidence/injected.py", "print('nope')")
    assert result.error is not None
    assert not (Path(require("EVIDENCE_PATH")) / "injected.py").exists()


def test_editing_evidence_is_refused():
    result = create_backend().edit("/evidence/infra/main.tf", "shipdb-primary", "tampered")
    assert result.error is not None
