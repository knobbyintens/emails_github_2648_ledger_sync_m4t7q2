# Real-Time Ledger Sync — ingestion worker
import json
import time

POSTING_KEY_PREFIX = "ledger"


def posting_key(event):
    """Deterministic key that makes ERP posting idempotent."""
    return f"{POSTING_KEY_PREFIX}:{event['account_id']}:{event['event_id']}"


def run_once(source, sink):
    for event in source.poll():
        sink.post(posting_key(event), json.dumps(event))
