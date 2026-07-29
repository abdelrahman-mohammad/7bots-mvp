import { Link, Route, Routes } from 'react-router-dom'

import ElementDetailPage from './pages/ElementDetailPage'
import ElementsPage from './pages/ElementsPage'
import RunPage from './pages/RunPage'
import VersionsPage from './pages/VersionsPage'

export default function App() {
  return (
    <main>
      <h1>ShipTrack As-Is Model</h1>
      <nav>
        <Link to="/">Run</Link> | <Link to="/elements">Elements</Link> |{' '}
        <Link to="/versions">Versions</Link>
      </nav>
      <Routes>
        <Route path="/" element={<RunPage />} />
        <Route path="/elements" element={<ElementsPage />} />
        <Route path="/elements/:elementId" element={<ElementDetailPage />} />
        <Route path="/versions" element={<VersionsPage />} />
      </Routes>
    </main>
  )
}
