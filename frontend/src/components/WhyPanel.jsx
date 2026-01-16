function WhyPanel({ why }) {
  if (!Array.isArray(why) || why.length === 0) return null;

  return (
    <div className="panel">
      {why.map((item, index) => {
        const direction = item?.direction ?? 'neutral';
        const percent = item?.percentage ?? item?.percent ?? '';
        const reason = item?.reason ?? '';

        return (
          <div key={index} className="why-row">
            <div className="why-meta">
              <span className="pill">{direction}</span>
              {percent && <span className="percent">{percent}</span>}
            </div>
            <div className="why-reason">{reason}</div>
          </div>
        );
      })}
    </div>
  );
}

export default WhyPanel;
