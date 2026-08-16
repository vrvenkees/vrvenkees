# ⛓️ Blockchain Infrastructure Monitor

A DevOps/SRE portfolio project for monitoring blockchain node infrastructure. Focus: reliability, observability, alerting and incident response — not crypto trading or financial advice.

## Goals
- Monitor node health and synchronization
- Expose infrastructure metrics to Prometheus
- Visualize health in Grafana
- Alert on node lag, RPC latency, peer count, CPU, memory and disk
- Demonstrate SLI/SLO, alerting and incident-response practices
- Run safely as a local lab without funds or private keys

## Architecture
```text
Blockchain node / RPC endpoint
            ↓
     Node health collector
            ↓
       Prometheus
        ↙        ↘
    Grafana   Alertmanager
                  ↓
             Notification
```

## Planned stack
Python / FastAPI • Prometheus • Grafana • Alertmanager • Docker Compose • Kubernetes • GitHub Actions

## Metrics
- `blockchain_latest_block` — latest observed block height
- `blockchain_block_age_seconds` — age of latest block
- `blockchain_rpc_latency_seconds` — RPC response latency
- `blockchain_peer_count` — connected peer count
- `blockchain_sync_status` — synchronization state
- `blockchain_up` — endpoint availability

## Roadmap
- [ ] Python health collector
- [ ] Prometheus metrics endpoint
- [ ] Docker Compose environment
- [ ] Grafana dashboard JSON
- [ ] Alertmanager rules
- [ ] Kubernetes deployment
- [ ] Multi-chain adapter interface
- [ ] CI tests and linting
- [ ] Incident/RCA examples

## Safety
This is an infrastructure/observability lab. It does not custody funds, request seed phrases, or execute financial transactions.

## License
MIT
