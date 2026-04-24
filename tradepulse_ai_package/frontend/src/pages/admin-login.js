import Link from 'next/link';
export default function AdminLogin(){ return <div className="form-wrap card"><h2>Admin Login</h2><input placeholder="Username" defaultValue="Abshira"/><input placeholder="Password" type="password"/><Link className="btn" href="/admin">Login as Admin</Link><p className="notice">For production, connect this form to /api/admin/login and use HTTPS.</p></div> }
