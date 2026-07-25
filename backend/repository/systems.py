from sqlalchemy import select
from sqlalchemy.orm import Session

from backend.tables import LegacySystem


def create_system(
    session: Session, system_id: str, name: str, description: str | None = None
) -> LegacySystem:
    system = LegacySystem(id=system_id, name=name, description=description)
    session.add(system)
    session.flush()
    return system


def get_system(session: Session, system_id: str) -> LegacySystem | None:
    return session.get(LegacySystem, system_id)


def list_systems(session: Session) -> list[LegacySystem]:
    return list(session.scalars(select(LegacySystem)))


def update_system(
    session: Session, system_id: str, name: str | None = None, description: str | None = None
) -> LegacySystem | None:
    system = session.get(LegacySystem, system_id)
    if system is None:
        return None
    if name is not None:
        system.name = name
    if description is not None:
        system.description = description
    session.flush()
    return system
