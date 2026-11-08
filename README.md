# Real-Time Ledger Sync

**Status: Released — v1.2.0 (2025-10-02)**

Reference implementation for the "Real-Time Ledger Sync" integration blueprint.

## What is included

- Durable outbox ingestion for billing ledger events
- Idempotent ERP posting adapter with deterministic posting keys
- Replay-safe checkpoint store
- Nightly reconciliation job with discrepancy reporting
- Integration tests covering retry, replay and duplicate-suppression paths

## Quick start

```bash
git clone https://github.com/knobbyintens/emails_github_2648_ledger_sync_m4t7q2.git
cd emails_github_2648_ledger_sync_m4t7q2
pip install -r requirements.txt
python -m src.ledger_sync --config config/local.yaml
```

## Repository layout

```
src/        ingestion worker, ERP adapter and checkpoint store
tests/      unit and integration tests
docs/       architecture notes and runbook
```

## License

MIT
