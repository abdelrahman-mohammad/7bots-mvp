from sqlalchemy import Engine, create_engine, text
from sqlalchemy.orm import Session, sessionmaker

from backend.config import database_url

IDENTITY_QUERY = "SELECT USER, current_database(), usesuper FROM pg_user WHERE usename = USER"


def create_db_engine() -> Engine:
    return create_engine(database_url(), pool_pre_ping=True)


def create_session() -> Session:
    return sessionmaker(bind=create_db_engine())()


def check_connection() -> dict[str, object]:
    with create_db_engine().connect() as conn:
        user, database, is_superuser = conn.execute(text(IDENTITY_QUERY)).one()
        conn.execute(text("CREATE TABLE _connection_check (id INT)"))
        conn.rollback()
    return {
        "user": user,
        "database": database,
        "superuser": is_superuser,
        "can_create_tables": True,
    }


if __name__ == "__main__":
    for key, value in check_connection().items():
        print(f"{key}: {value}")
