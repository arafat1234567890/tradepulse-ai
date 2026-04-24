import Layout from '../components/Layout';
import SignalCard from '../components/SignalCard';

const signal = {symbol:'BTC/USDT',direction:'BUY',confidence:74,entry:'68,200 - 68,600',stop_loss:'67,450',take_profit:'70,000',risk_reward:'1:2',confirmations:[{name:'RSI',status:'confirmed'},{name:'MACD',status:'confirmed'},{name:'Trend',status:'bullish'},{name:'News',status:'neutral'}]};

export default function Dashboard(){
 return <Layout><h1>Dashboard</h1><div className="grid"><div className="card"><h3>Account Status</h3><p>Active subscription</p></div><div className="card"><h3>Risk Level</h3><p>Moderate</p></div><div className="card"><h3>Signals Today</h3><p>24 generated</p></div></div><h2>Current Best Signal</h2><SignalCard signal={signal}/><div className="card"><h3>Market Background Check</h3><p>Global news: neutral. Volatility: medium. Economic events: check calendar before trading USD pairs.</p></div></Layout>
}
