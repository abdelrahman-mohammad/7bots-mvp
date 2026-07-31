import sys

from backend.db import create_session
from backend.repository.systems import create_system, get_system


def seed(system_id, name):
    session = create_session()
    try:
        if get_system(session, system_id):
            return f"{system_id} already exists"
        create_system(session, system_id, name)
        session.commit()
        return f"created {system_id}"
    finally:
        session.close()


if __name__ == "__main__":
    system_id = sys.argv[1]
    name = sys.argv[2] if len(sys.argv) > 2 else system_id
    print(seed(system_id, name))
