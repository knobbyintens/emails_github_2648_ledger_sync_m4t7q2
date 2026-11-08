from src.ledger_sync import posting_key


def test_posting_key_is_stable():
    event = {"account_id": "A100", "event_id": "evt-42"}
    assert posting_key(event) == posting_key(dict(event))
