import Link from 'next/link';

export default function Home() {
  return (
    <div className="hero">
      <nav className="nav">
        <strong>TradePulse AI</strong>
        <div className="nav-links">
          <Link href="/login">Login</Link>
          <Link className="btn" href="/signup">Start for $33</Link>
        </div>
      </nav>
      <section className="hero-grid">
        <div>
          <h1>AI-assisted trading signals with multi-layer confirmation.</h1>
          <p>Analyze technical indicators, global news, sentiment, volatility, and risk before acting. Built for disciplined traders, not gambling.</p>
          <div className="btn-row">
            <Link href="/signup" className="btn">Create Account</Link>
            <Link href="/dashboard" className="btn secondary">View Demo</Link>
          </div>
          <p className="notice">Educational analysis only. No profits or accuracy are guaranteed.</p>
        </div>
        <div className="card">
          <h2>Live Signal Preview</h2>
          <p>BTC/USDT</p>
          <h3>BUY · 74% confidence</h3>
          <p>Confirmed by RSI, MACD, trend structure, and neutral news sentiment.</p>
        </div>
      </section>
    </div>
  );
}
