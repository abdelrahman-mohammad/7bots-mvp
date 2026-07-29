const BASE_URL = import.meta.env.VITE_API_BASE_URL
const API_KEY = import.meta.env.VITE_API_KEY

export type ElementSummary = {
  id: string
  layer: string
  archimate_type: string
  name: string
  git_path: string
  current_commit: string
}

export type Job = {
  id: number
  system_id: string
  status: string
  run_id: string | null
  error_message: string | null
}

export type ArtifactVersion = {
  commit_sha: string
  tag: string | null
  run_id: string | null
  approval_status: string
}

async function request(path: string, options: RequestInit = {}) {
  const response = await fetch(BASE_URL + path, {
    ...options,
    headers: { "X-API-Key": API_KEY, "Content-Type": "application/json" },
  })
  if (!response.ok) {
    throw new Error(response.status + " " + response.statusText)
  }
  return response.json()
}

export function triggerIngestion(systemId: string): Promise<{ job_id: number }> {
  return request("/systems/" + systemId + "/ingest", { method: "POST" })
}

export function getJob(jobId: number): Promise<Job> {
  return request("/jobs/" + jobId)
}

export function listElements(systemId: string, layer?: string): Promise<ElementSummary[]> {
  const query = layer ? "?layer=" + layer : ""
  return request("/systems/" + systemId + "/elements" + query)
}

export function getElement(elementId: string): Promise<unknown> {
  return request("/elements/" + elementId)
}

export function listArtifactVersions(systemId: string): Promise<ArtifactVersion[]> {
  return request("/systems/" + systemId + "/artifact-versions")
}
