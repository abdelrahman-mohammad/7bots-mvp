from backend.repository import artifact_versions, elements, evidence, jobs, systems


def test_create_and_get_system(session):
    systems.create_system(session, "billing", "Billing System")
    found = systems.get_system(session, "billing")
    assert found.name == "Billing System"


def test_get_missing_system_returns_none(session):
    assert systems.get_system(session, "does-not-exist") is None


def test_update_system(session, system):
    systems.update_system(session, system.id, name="Renamed")
    assert systems.get_system(session, system.id).name == "Renamed"


def upsert(session, system_id, name, commit):
    return elements.upsert_element(
        session,
        element_id="app-payment-service",
        system_id=system_id,
        layer="application",
        archimate_type="ApplicationComponent",
        name=name,
        git_path="systems/claims-system/as-is/application/app-payment-service.json",
        current_commit=commit,
    )


def test_upsert_element_inserts_then_updates(session, system):
    upsert(session, system.id, "Payment Service", "aaa111")
    upsert(session, system.id, "Payment Service Renamed", "bbb222")

    all_elements = elements.list_elements(session, system.id)
    assert len(all_elements) == 1
    assert all_elements[0].name == "Payment Service Renamed"
    assert all_elements[0].current_commit == "bbb222"


def test_list_elements_filters_by_layer(session, system):
    upsert(session, system.id, "Payment Service", "aaa111")
    assert len(elements.list_elements(session, system.id, layer="application")) == 1
    assert len(elements.list_elements(session, system.id, layer="business")) == 0


def test_create_artifact_version_and_approve(session, system):
    artifact_versions.create_artifact_version(session, system.id, "sha123", "as-is", "agent")
    version = artifact_versions.get_artifact_version(session, "sha123")
    assert version.approval_status == "pending"
    assert version.approved_at is None

    artifact_versions.set_approval(session, "sha123", "approved", approved_by="abdel")
    version = artifact_versions.get_artifact_version(session, "sha123")
    assert version.approval_status == "approved"
    assert version.approved_at is not None


def test_approving_twice_is_idempotent(session, system):
    artifact_versions.create_artifact_version(session, system.id, "sha123", "as-is", "agent")
    first = artifact_versions.set_approval(session, "sha123", "approved", approved_by="abdel")
    approved_at = first.approved_at

    second = artifact_versions.set_approval(session, "sha123", "approved", approved_by="abdel")

    assert second.approved_at == approved_at
    assert len(artifact_versions.list_artifact_versions(session, system.id)) == 1


def test_job_status_transitions(session, system):
    job = jobs.create_job(session, system.id, "as-is")
    assert job.status == "queued"
    assert job.started_at is None

    jobs.update_job_status(session, job.id, "running", run_id="run-1")
    assert job.status == "running"
    assert job.started_at is not None
    assert job.finished_at is None

    jobs.update_job_status(session, job.id, "succeeded")
    assert job.finished_at is not None


def test_marking_job_failed_twice_is_idempotent(session, system):
    job = jobs.create_job(session, system.id, "as-is")
    jobs.update_job_status(session, job.id, "failed", error_message="boom")
    finished_at = job.finished_at

    jobs.update_job_status(session, job.id, "failed", error_message="boom")

    assert job.finished_at == finished_at
    assert job.error_message == "boom"
    assert job.status == "failed"


def test_update_missing_job_returns_none(session):
    assert jobs.update_job_status(session, 999999, "failed") is None


def test_evidence_sources(session, system):
    evidence.create_evidence_source(session, system.id, "code", "/evidence/code", "Sample repo")
    evidence.create_evidence_source(session, system.id, "infra", "/evidence/infra")

    sources = evidence.list_evidence_sources(session, system.id)
    assert len(sources) == 2

    evidence.update_evidence_source(session, sources[0].id, "Updated description")
    assert evidence.get_evidence_source(session, sources[0].id).description == "Updated description"
