function ExplorePage() {
  return (
    <section id="explore" className="explore">
      <div className="explore-head">
        <p className="eyebrow">Choose a path</p>
        <h2>Start free or see paid options</h2>
        <p className="subtext">Free gets you straight into the chat. Paid is coming soon.</p>
      </div>

      <div className="plan-grid">
        <div className="plan-card">
          <h3>Free</h3>
          <p>Ask questions and view answers and tables.</p>
          <a href="#chat" className="btn">Start Free</a>
        </div>

        <div className="plan-card">
          <h3>Paid</h3>
          <p>Advanced insights, export, and priority features.</p>
          <a href="#under-process" className="btn ghost">Go Pro</a>
        </div>
      </div>
    </section>
  );
}

export default ExplorePage;
