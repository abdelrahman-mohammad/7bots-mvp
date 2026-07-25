import pytest
from sqlalchemy.orm import Session

from backend.db import create_db_engine


@pytest.fixture
def session():
    engine = create_db_engine()
    connection = engine.connect()
    transaction = connection.begin()
    db = Session(bind=connection)

    yield db

    db.close()
    transaction.rollback()
    connection.close()


@pytest.fixture
def system(session):
    from backend.repository.systems import create_system

    return create_system(session, "claims-system", "Claims System", "Test fixture")
