import Link from 'next/link';

export default function Login(){
 return <div className="form-wrap card"><h2>User Login</h2><input placeholder="Email"/><input placeholder="Password" type="password"/><Link href="/dashboard" className="btn">Login</Link><p>No account? <Link href="/signup">Sign up</Link></p></div>
}
