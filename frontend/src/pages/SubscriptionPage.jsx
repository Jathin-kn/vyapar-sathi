function SubscriptionPage() {
  return (
    <section id="subscribe" className="subscription">
      <div className="sub-head">
        <p className="eyebrow">Plans</p>
        <h2>Pick the plan that fits</h2>
        <p className="subtext">Simple pricing for teams that want fast insights.</p>
      </div>

      <div className="sub-card">
        <div className="sub-tier">Growth</div>
        <div className="sub-price">
          <span className="currency">$</span>
          <span className="amount">49</span>
          <span className="per">/mo</span>
        </div>
        <ul className="sub-list">
          <li>Unlimited questions</li>
          <li>Why analysis on key metrics</li>
          <li>CSV table export</li>
          <li>Email support</li>
        </ul>
        <a className="btn" href="#chat">Start chatting</a>
      </div>
    </section>
  );
}

export default SubscriptionPage;
