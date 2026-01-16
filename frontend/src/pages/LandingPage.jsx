function LandingPage() {
  return (
    <section className="landing">
      <nav className="nav">
        <div className="brand">Vyapar Sathi</div>
        <div className="nav-actions">
          <a href="#explore" className="btn ghost">Explore the app</a>
          <a href="#chat" className="link">Jump to chat</a>
        </div>
      </nav>

      <div className="landing-hero">
        <div className="copy">
          <p className="eyebrow">Analytics copilot</p>
          <h1>Answers, trends, and reasons in one chat.</h1>
          <p className="lead">
            Ask plain-language questions about your business and instantly see answers,
            tables, and the why behind the change.
          </p>
          <div className="actions">
            <a href="#explore" className="btn">Explore the app</a>
            <a href="#chat" className="btn ghost">Try the chat</a>
          </div>
        </div>
        <div className="hero-card">
          <p className="badge">Preview</p>
          <p className="hero-metric">Ask about your metrics</p>
          <p className="hero-foot">Type a question → Get the why</p>
        </div>
      </div>

      <div className="feature-grid">
        <div className="feature">
          <h3>Natural questions</h3>
          <p>Ask like a human—no SQL. We translate intent and fetch the right slice.</p>
        </div>
        <div className="feature">
          <h3>Why it moved</h3>
          <p>See direction, percent change, and concise reasoning in seconds.</p>
        </div>
        <div className="feature">
          <h3>Tables on demand</h3>
          <p>View the rows behind the answer to validate and export quickly.</p>
        </div>
      </div>
    </section>
  );
}

export default LandingPage;
