import Link from 'next/link';

export default function Layout({ children }) {
  return (
    <div className="app-shell">
      <aside className="sidebar">
        <h2>TradePulse AI</h2>
        <Link href="/dashboard">Dashboard</Link>
        <Link href="/signals">Signals</Link>
        <Link href="/analysis">Analysis</Link>
        <Link href="/journal">Journal</Link>
        <Link href="/strategies">Strategies</Link>
        <Link href="/admin">Admin</Link>
      </aside>
      <main className="content">{children}</main>
    </div>
  );
}
