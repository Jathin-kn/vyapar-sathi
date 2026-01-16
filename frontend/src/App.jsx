import './App.css'
import LandingPage from './pages/LandingPage'
import ExplorePage from './pages/ExplorePage'
import UnderProcessPage from './pages/UnderProcessPage'
import ChatPage from './pages/ChatPage'

function App() {
  return (
    <main className="page">
      <LandingPage />
      <ExplorePage />
      <UnderProcessPage />
      <ChatPage />
    </main>
  )
}

export default App
