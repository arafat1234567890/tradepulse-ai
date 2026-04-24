import Layout from '../components/Layout';
import SignalCard from '../components/SignalCard';
const signals = ['BTC/USDT','ETH/USDT','EUR/USD','XAU/USD','GBP/USD'].map((s,i)=>({symbol:s,direction:i%2?'SELL':'BUY',confidence:68+i*3,entry:'Market zone',stop_loss:'Auto volatility SL',take_profit:'Auto risk/reward TP',risk_reward:'1:2',confirmations:[{name:'RSI',status:'checked'},{name:'MACD',status:'checked'},{name:'MA',status:'checked'},{name:'News',status:'checked'}]}));
export default function Signals(){ return <Layout><h1>Live Signals</h1>{signals.map(s=><SignalCard key={s.symbol} signal={s}/>)}</Layout> }
