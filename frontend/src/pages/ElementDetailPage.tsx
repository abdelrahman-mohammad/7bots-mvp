import { useEffect, useState } from 'react'
import { Link, useParams } from 'react-router-dom'

import { getElement, type ElementDetail, type Evidence } from '../api'

const EVIDENCE_REPO = import.meta.env.VITE_EVIDENCE_REPO_URL

function githubLink(locator: string) {
  const parts = locator.split(':')
  const path = parts[0].replace('/evidence/', 'test-fixtures/evidence/')
  const url = EVIDENCE_REPO + '/blob/main/' + path
  if (parts.length < 2) {
    return url
  }
  const lines = parts[1].split('-')
  return url + '#L' + lines[0] + (lines[1] ? '-L' + lines[1] : '')
}

function Citation({ evidence }: { evidence: Evidence }) {
  return (
    <li>
      <a href={githubLink(evidence.locator)} target="_blank" rel="noreferrer">
        {evidence.locator}
      </a>
      <blockquote>{evidence.excerpt}</blockquote>
      <small>{evidence.source_type}</small>
    </li>
  )
}

export default function ElementDetailPage() {
  const { elementId } = useParams()
  const [element, setElement] = useState<ElementDetail | null>(null)
  const [problem, setProblem] = useState<string | null>(null)

  useEffect(() => {
    if (!elementId) {
      return
    }
    setElement(null)
    setProblem(null)
    getElement(elementId)
      .then(setElement)
      .catch((failure) => setProblem(String(failure)))
  }, [elementId])

  if (problem) {
    return <p>Could not load {elementId}: {problem}</p>
  }
  if (!element) {
    return <p>Loading {elementId}...</p>
  }

  const relationships = element.relationships ?? []

  return (
    <section>
      <h2>{element.name}</h2>
      <p>
        {element.archimate_type} in the {element.layer} layer, recorded as {element.confidence}.
      </p>
      <p>{element.documentation}</p>

      <h3>Evidence ({element.evidence.length})</h3>
      <ul>
        {element.evidence.map((evidence) => (
          <Citation key={evidence.locator + evidence.excerpt} evidence={evidence} />
        ))}
      </ul>

      <h3>Relationships ({relationships.length})</h3>
      {relationships.length === 0 && <p>None recorded.</p>}
      <ul>
        {relationships.map((relationship) => (
          <li key={relationship.type + relationship.target_id}>
            {relationship.type} to{' '}
            <Link to={'/elements/' + relationship.target_id}>{relationship.target_id}</Link>
            <ul>
              {relationship.evidence.map((evidence) => (
                <Citation key={evidence.locator + evidence.excerpt} evidence={evidence} />
              ))}
            </ul>
          </li>
        ))}
      </ul>

      <p>
        <Link to="/elements">Back to all elements</Link>
      </p>
    </section>
  )
}
