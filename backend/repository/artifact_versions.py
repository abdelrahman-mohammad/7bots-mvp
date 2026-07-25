from datetime import UTC, datetime

from sqlalchemy import select
from sqlalchemy.orm import Session

from backend.tables import ArtifactVersion


def create_artifact_version(
    session: Session,
    system_id: str,
    commit_sha: str,
    phase: str,
    author_type: str,
    tag: str | None = None,
    run_id: str | None = None,
) -> ArtifactVersion:
    version = ArtifactVersion(
        system_id=system_id,
        commit_sha=commit_sha,
        phase=phase,
        author_type=author_type,
        tag=tag,
        run_id=run_id,
    )
    session.add(version)
    session.flush()
    return version


def get_artifact_version(session: Session, commit_sha: str) -> ArtifactVersion | None:
    query = select(ArtifactVersion).where(ArtifactVersion.commit_sha == commit_sha)
    return session.scalars(query).first()


def list_artifact_versions(session: Session, system_id: str) -> list[ArtifactVersion]:
    query = select(ArtifactVersion).where(ArtifactVersion.system_id == system_id)
    return list(session.scalars(query))


def set_approval(
    session: Session, commit_sha: str, approval_status: str, approved_by: str | None = None
) -> ArtifactVersion | None:
    version = get_artifact_version(session, commit_sha)
    if version is None:
        return None
    version.approval_status = approval_status
    if approved_by is not None:
        version.approved_by = approved_by
    if approval_status == "approved" and version.approved_at is None:
        version.approved_at = datetime.now(UTC)
    session.flush()
    return version
