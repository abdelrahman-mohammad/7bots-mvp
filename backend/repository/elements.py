from sqlalchemy import select
from sqlalchemy.orm import Session

from backend.tables import ModelElementIndex


def upsert_element(
    session: Session,
    element_id: str,
    system_id: str,
    layer: str,
    archimate_type: str,
    name: str,
    git_path: str,
    current_commit: str,
) -> ModelElementIndex:
    element = session.get(ModelElementIndex, element_id)
    if element is None:
        element = ModelElementIndex(id=element_id, system_id=system_id)
        session.add(element)
    element.layer = layer
    element.archimate_type = archimate_type
    element.name = name
    element.git_path = git_path
    element.current_commit = current_commit
    session.flush()
    return element


def get_element(session: Session, element_id: str) -> ModelElementIndex | None:
    return session.get(ModelElementIndex, element_id)


def list_elements(
    session: Session, system_id: str, layer: str | None = None
) -> list[ModelElementIndex]:
    query = select(ModelElementIndex).where(ModelElementIndex.system_id == system_id)
    if layer is not None:
        query = query.where(ModelElementIndex.layer == layer)
    return list(session.scalars(query))
