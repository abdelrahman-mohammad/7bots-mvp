from sqlalchemy import select
from sqlalchemy.orm import Session

from backend.tables import EvidenceSource


def create_evidence_source(
    session: Session,
    system_id: str,
    source_type: str,
    location: str,
    description: str | None = None,
) -> EvidenceSource:
    source = EvidenceSource(
        system_id=system_id,
        source_type=source_type,
        location=location,
        description=description,
    )
    session.add(source)
    session.flush()
    return source


def get_evidence_source(session: Session, source_id: int) -> EvidenceSource | None:
    return session.get(EvidenceSource, source_id)


def list_evidence_sources(session: Session, system_id: str) -> list[EvidenceSource]:
    query = select(EvidenceSource).where(EvidenceSource.system_id == system_id)
    return list(session.scalars(query))


def update_evidence_source(
    session: Session, source_id: int, description: str
) -> EvidenceSource | None:
    source = session.get(EvidenceSource, source_id)
    if source is None:
        return None
    source.description = description
    session.flush()
    return source
