from cash_flow import TRANSACTIONS_FILE, add_transaction, balance, load_transactions
from pathlib import Path
import json
import pytest


def test_add_and_balance(tmp_path, monkeypatch):
    temp_file = tmp_path / "transactions.json"
    monkeypatch.setattr("cash_flow.TRANSACTIONS_FILE", temp_file)

    add_transaction(200, "venda")
    add_transaction(-50, "despesa")

    assert temp_file.exists()
    with open(temp_file) as f:
        data = json.load(f)
    assert len(data) == 2
    assert balance() == 150

