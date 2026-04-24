export default function SignalCard({ signal }) {
  return (
    <div className="card signal-card">
      <div className="row between">
        <h3>{signal.symbol}</h3>
        <span className={`badge ${signal.direction?.toLowerCase()}`}>{signal.direction}</span>
      </div>
      <p>Confidence: <strong>{signal.confidence}%</strong></p>
      <p>Entry: {signal.entry}</p>
      <p>Stop Loss: {signal.stop_loss}</p>
      <p>Take Profit: {signal.take_profit}</p>
      <p>Risk/Reward: {signal.risk_reward}</p>
      <div className="mini-list">
        {signal.confirmations?.map((item) => (
          <span key={item.name}>{item.name}: {item.status}</span>
        ))}
      </div>
    </div>
  );
}
