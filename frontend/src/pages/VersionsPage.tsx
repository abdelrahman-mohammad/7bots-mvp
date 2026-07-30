import { useEffect, useState } from 'react'

import { listArtifactVersions, type ArtifactVersion } from '../api'

const SYSTEM_ID = 'shiptrack'
const MODEL_REPO = import.meta.env.VITE_MODEL_REPO_URL

function pullRequestNumber(tag: string | null) {
  if (!tag || !tag.startsWith('pr-')) {
    return null
  }
  return tag.slice(3)
}

export default function VersionsPage() {
  const [versions, setVersions] = useState<ArtifactVersion[]>([])
  const [problem, setProblem] = useState<string | null>(null)

  useEffect(() => {
    listArtifactVersions(SYSTEM_ID)
      .then(setVersions)
      .catch((failure) => setProblem(String(failure)))
  }, [])

  if (problem) {
    return <p>Could not load versions: {problem}</p>
  }

  return (
    <section>
      <h2>Artifact versions and PR status</h2>
      <p>{versions.length} versions of the model have been committed.</p>

      <table>
        <thead>
          <tr>
            <th>Commit</th>
            <th>Phase</th>
            <th>Run</th>
            <th>Approval</th>
            <th>Pull request</th>
          </tr>
        </thead>
        <tbody>
          {versions.map((version) => {
            const number = pullRequestNumber(version.tag)
            return (
              <tr key={version.commit_sha}>
                <td>
                  <a
                    href={MODEL_REPO + '/commit/' + version.commit_sha}
                    target="_blank"
                    rel="noreferrer"
                  >
                    {version.commit_sha.slice(0, 8)}
                  </a>
                </td>
                <td>{version.phase}</td>
                <td>{version.run_id}</td>
                <td>{version.approval_status}</td>
                <td>
                  {number ? (
                    <a
                      href={MODEL_REPO + '/pull/' + number}
                      target="_blank"
                      rel="noreferrer"
                    >
                      #{number}
                    </a>
                  ) : (
                    'none'
                  )}
                </td>
              </tr>
            )
          })}
        </tbody>
      </table>
    </section>
  )
}
