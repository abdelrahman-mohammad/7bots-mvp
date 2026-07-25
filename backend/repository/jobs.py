from datetime import UTC, datetime

from sqlalchemy import select
from sqlalchemy.orm import Session

from backend.tables import Job

TERMINAL_STATUSES = ("succeeded", "failed")


def create_job(session: Session, system_id: str, phase: str) -> Job:
    job = Job(system_id=system_id, phase=phase, status="queued")
    session.add(job)
    session.flush()
    return job


def get_job(session: Session, job_id: int) -> Job | None:
    return session.get(Job, job_id)


def list_jobs(session: Session, system_id: str) -> list[Job]:
    return list(session.scalars(select(Job).where(Job.system_id == system_id)))


def update_job_status(
    session: Session,
    job_id: int,
    status: str,
    run_id: str | None = None,
    error_message: str | None = None,
) -> Job | None:
    job = session.get(Job, job_id)
    if job is None:
        return None
    job.status = status
    if run_id is not None:
        job.run_id = run_id
    if error_message is not None:
        job.error_message = error_message
    if status == "running" and job.started_at is None:
        job.started_at = datetime.now(UTC)
    if status in TERMINAL_STATUSES and job.finished_at is None:
        job.finished_at = datetime.now(UTC)
    session.flush()
    return job
