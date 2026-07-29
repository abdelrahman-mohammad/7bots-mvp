import { useEffect, useState } from 'react'
import { Link } from 'react-router-dom'

import { listElements, type ElementSummary } from '../api'

const SYSTEM_ID = 'shiptrack'
const LAYERS = ['motivation', 'strategy', 'business', 'application', 'technology']

export default function ElementsPage() {
  const [elements, setElements] = useState<ElementSummary[]>([])
  const [problem, setProblem] = useState<string | null>(null)

  useEffect(() => {
    listElements(SYSTEM_ID)
      .then(setElements)
      .catch((failure) => setProblem(String(failure)))
  }, [])

  if (problem) {
    return <p>Could not load elements: {problem}</p>
  }

  return (
    <section>
      <h2>Model elements</h2>
      <p>{elements.length} elements in the approved model.</p>

      {LAYERS.map((layer) => {
        const inLayer = elements.filter((element) => element.layer === layer)
        if (inLayer.length === 0) {
          return null
        }
        return (
          <div key={layer}>
            <h3>
              {layer} ({inLayer.length})
            </h3>
            <ul>
              {inLayer.map((element) => (
                <li key={element.id}>
                  <Link to={'/elements/' + element.id}>{element.name}</Link>{' '}
                  <small>{element.archimate_type}</small>
                </li>
              ))}
            </ul>
          </div>
        )
      })}
    </section>
  )
}
