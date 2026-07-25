from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Text, func
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class LegacySystem(Base):
    __tablename__ = "legacy_systems"

    id = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(Text)


class ModelElementIndex(Base):
    __tablename__ = "model_element_index"

    id = Column(String, primary_key=True)
    system_id = Column(String, ForeignKey("legacy_systems.id"), nullable=False)
    layer = Column(String, nullable=False)
    archimate_type = Column(String, nullable=False)
    name = Column(String, nullable=False)
    git_path = Column(String, nullable=False)
    current_commit = Column(String, nullable=False)
    updated_at = Column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False
    )


class ArtifactVersion(Base):
    __tablename__ = "artifact_versions"

    id = Column(Integer, primary_key=True)
    system_id = Column(String, ForeignKey("legacy_systems.id"), nullable=False)
    commit_sha = Column(String, nullable=False)
    phase = Column(String, nullable=False)
    tag = Column(String)
    author_type = Column(String, nullable=False)
    run_id = Column(String)
    approval_status = Column(String, server_default="pending", nullable=False)
    approved_by = Column(String)
    approved_at = Column(DateTime(timezone=True))
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)


class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True)
    system_id = Column(String, ForeignKey("legacy_systems.id"), nullable=False)
    phase = Column(String, nullable=False)
    status = Column(String, server_default="queued", nullable=False)
    run_id = Column(String)
    error_message = Column(Text)
    started_at = Column(DateTime(timezone=True))
    finished_at = Column(DateTime(timezone=True))


class EvidenceSource(Base):
    __tablename__ = "evidence_sources"

    id = Column(Integer, primary_key=True)
    system_id = Column(String, ForeignKey("legacy_systems.id"), nullable=False)
    source_type = Column(String, nullable=False)
    location = Column(String, nullable=False)
    description = Column(Text)
    added_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
