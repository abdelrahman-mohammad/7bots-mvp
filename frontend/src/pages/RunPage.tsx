import { useEffect, useState } from 'react'

import { getJob, triggerIngestion, type Job } from '../api'

const SYSTEM_ID = 'shiptrack'
const FINISHED = ['succeeded', 'failed']

export default function RunPage() {
  const [jobId, setJobId] = useState<number | null>(null)
  const [job, setJob] = useState<Job | null>(null)
  const [problem, setProblem] = useState<string | null>(null)

  async function start() {
    setProblem(null)
    setJob(null)
    setJobId(null)
    try {
      const started = await triggerIngestion(SYSTEM_ID)
      setJobId(started.job_id)
    } catch (failure) {
      setProblem(String(failure))
    }
  }

  useEffect(() => {
    if (jobId === null) {
      return
    }

    async function poll() {
      try {
        const latest = await getJob(jobId as number)
        setJob(latest)
        if (FINISHED.includes(latest.status)) {
          clearInterval(timer)
        }
      } catch (failure) {
        setProblem(String(failure))
        clearInterval(timer)
      }
    }

    const timer = setInterval(poll, 2000)
    poll()
    return () => clearInterval(timer)
  }, [jobId])

  const running = job !== null && !FINISHED.includes(job.status)

  return (
    <section>
      <h2>Trigger run and job status</h2>

      <button onClick={start} disabled={running}>
        Run ingestion
      </button>

      {problem && <p>Could not reach the API: {problem}</p>}

      {jobId !== null && (
        <dl>
          <dt>Job</dt>
          <dd>{jobId}</dd>
          <dt>Status</dt>
          <dd>{job ? job.status : 'queued'}</dd>
          {job?.run_id && (
            <>
              <dt>LangSmith run</dt>
              <dd>{job.run_id}</dd>
            </>
          )}
          {job?.status === 'failed' && (
            <>
              <dt>Why it failed</dt>
              <dd>{job.error_message}</dd>
            </>
          )}
        </dl>
      )}
    </section>
  )
}
