# NovaX — Exchange Sandbox

A visually rich, fully client-side crypto exchange sandbox for portfolio, product and systems-engineering work. Inspired by the interaction patterns of professional trading terminals: live market ticker, chart, order book, order form, open orders, trade history and assets. Current balances and orders are simulated in the browser.

## What works
- Live simulated market-price ticks
- Interactive price chart
- Simulated order book
- Buy/sell tabs
- Market/limit order selector
- Demo order execution
- Simulated USDT balance
- Quick percentage sizing
- Open orders / history / assets views
- Cancel and clear actions
- Watchlist toggle
- Demo-account and profile dialogs
- Responsive layout
- LocalStorage persistence

## Safety
NovaX is currently a **sandbox**. It does not accept deposits, custody assets, connect wallets, sign transactions, or execute real trades. No seed phrases or private keys are requested.

## Product roadmap
1. Separate matching engine service
2. WebSocket market-data service
3. PostgreSQL ledger and audit trail
4. Authentication and role-based access
5. Testnet integration
6. Observability with Prometheus/Grafana
7. Security and DevSecOps pipeline
8. Compliance architecture before any real-asset launch

## Design research
The terminal layout intentionally follows common professional patterns: chart + order book + order form + trade history, customizable timeframes and responsive widgets. Kraken Pro documents customizable widgets, order-book interaction and live charting; Coinbase Advanced documents real-time order books, advanced order types and TradingView-powered charts.

## License
MIT
