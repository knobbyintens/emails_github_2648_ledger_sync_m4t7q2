# Architecture

Billing outbox -> ingestion worker -> ERP adapter -> ERP ledger.

The checkpoint store records the last committed outbox offset. Replaying from
an earlier offset is safe because every posting carries a deterministic key.
