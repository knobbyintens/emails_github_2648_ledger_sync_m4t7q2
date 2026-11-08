# ERP posting adapter for the ledger sync blueprint
class ErpAdapter:
    def __init__(self, client):
        self.client = client

    def post(self, key, payload):
        # The ERP accepts an idempotency key; a repeated key is a no-op.
        return self.client.post_journal(posting_key=key, body=payload)
