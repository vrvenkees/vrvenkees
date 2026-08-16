"""Safe blockchain RPC health collector for the portfolio lab.

Set RPC_URL to a public/test endpoint. No wallet keys or signing are used.
"""
import os
import time
from typing import Optional

import requests
from prometheus_client import Gauge, start_http_server

RPC_URL = os.getenv("RPC_URL", "https://cloudflare-eth.com")
POLL_SECONDS = int(os.getenv("POLL_SECONDS", "15"))

UP = Gauge("blockchain_up", "Whether the RPC endpoint is reachable")
RPC_LATENCY = Gauge("blockchain_rpc_latency_seconds", "RPC response latency")
LATEST_BLOCK = Gauge("blockchain_latest_block", "Latest observed block number")
BLOCK_AGE = Gauge("blockchain_block_age_seconds", "Approximate age of latest block")


def rpc(method: str, params: Optional[list] = None):
    started = time.perf_counter()
    response = requests.post(
        RPC_URL,
        json={"jsonrpc": "2.0", "id": 1, "method": method, "params": params or []},
        timeout=8,
    )
    RPC_LATENCY.set(time.perf_counter() - started)
    response.raise_for_status()
    payload = response.json()
    if "error" in payload:
        raise RuntimeError(payload["error"])
    return payload["result"]


def collect() -> None:
    try:
        block_hex = rpc("eth_blockNumber")
        block_number = int(block_hex, 16)
        LATEST_BLOCK.set(block_number)
        UP.set(1)
        # The JSON-RPC blockNumber call is deliberately used as the portable
        # baseline. A future adapter can fetch block timestamps to calculate
        # precise block age for each chain.
        BLOCK_AGE.set(0)
    except Exception as exc:
        UP.set(0)
        print(f"collector error: {exc}")


if __name__ == "__main__":
    start_http_server(int(os.getenv("METRICS_PORT", "9105")))
    while True:
        collect()
        time.sleep(POLL_SECONDS)
