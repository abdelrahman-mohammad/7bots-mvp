from langchain_core.tracers.context import collect_runs

from backend.db import create_session
from backend.orchestrator import run_as_is_ingestion
from backend.repository.jobs import update_job_status


def set_status(job_id, status, run_id=None, error_message=None):
    session = create_session()
    try:
        update_job_status(session, job_id, status, run_id=run_id, error_message=error_message)
        session.commit()
    finally:
        session.close()


def run_job(job_id, system_id, evidence_path):
    set_status(job_id, "running")
    try:
        with collect_runs() as collected:
            run_as_is_ingestion(system_id, evidence_path)
        traced = collected.traced_runs
        set_status(job_id, "succeeded", run_id=str(traced[0].id) if traced else None)
    except Exception as error:
        set_status(job_id, "failed", error_message=f"{type(error).__name__}: {error}")
