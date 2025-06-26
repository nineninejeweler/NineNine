diff --git a//dev/null b/cash_flow.py
index 0000000000000000000000000000000000000000..02f15743e5fd6bd12b477a838725a4f1ccc34936 100644
--- a//dev/null
+++ b/cash_flow.py
@@ -0,0 +1,65 @@
+import argparse
+import json
+from datetime import date
+from pathlib import Path
+
+TRANSACTIONS_FILE = Path("transactions.json")
+
+def load_transactions():
+    if TRANSACTIONS_FILE.exists():
+        with open(TRANSACTIONS_FILE, "r") as f:
+            return json.load(f)
+    return []
+
+def save_transactions(transactions):
+    with open(TRANSACTIONS_FILE, "w") as f:
+        json.dump(transactions, f, indent=2)
+
+def add_transaction(amount, description):
+    transactions = load_transactions()
+    transactions.append({
+        "date": date.today().isoformat(),
+        "description": description,
+        "amount": amount
+    })
+    save_transactions(transactions)
+
+
+def balance():
+    transactions = load_transactions()
+    return sum(t["amount"] for t in transactions)
+
+
+def list_transactions():
+    transactions = load_transactions()
+    for t in transactions:
+        print(f"{t['date']} - {t['description']}: {t['amount']:.2f}")
+    print(f"Balance: {balance():.2f}")
+
+
+def main():
+    parser = argparse.ArgumentParser(description="Nine Nine Cash Flow")
+    subparsers = parser.add_subparsers(dest="command", required=True)
+
+    income_parser = subparsers.add_parser("add-income", help="Add income transaction")
+    income_parser.add_argument("amount", type=float, help="Amount of income")
+    income_parser.add_argument("description", help="Description of income")
+
+    expense_parser = subparsers.add_parser("add-expense", help="Add expense transaction")
+    expense_parser.add_argument("amount", type=float, help="Amount of expense")
+    expense_parser.add_argument("description", help="Description of expense")
+
+    subparsers.add_parser("list", help="List transactions and balance")
+
+    args = parser.parse_args()
+
+    if args.command == "add-income":
+        add_transaction(abs(args.amount), args.description)
+    elif args.command == "add-expense":
+        add_transaction(-abs(args.amount), args.description)
+    elif args.command == "list":
+        list_transactions()
+
+
+if __name__ == "__main__":
+    main()

