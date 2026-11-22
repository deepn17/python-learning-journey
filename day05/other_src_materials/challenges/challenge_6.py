# Challenge 6 — Explicit parameter boundaries
#Design a transaction-registration API whose signature prevents ambiguous or error-prone calls by enforcing positional-only, positional-or-keyword, and keyword-only parameter rules.
# Business requirements
# •	Require transaction_id and amount positionally.
# •	Allow transaction_type to be positional or keyword-based.
# •	Require currency to be supplied by keyword.
# •	Default status to PENDING when omitted.

# Technical requirements
# •	Implement `register_transaction(transaction_id, amount, /, transaction_type, *, currency, status="PENDING")`.
# •	Do not duplicate Python’s own argument binding checks unnecessarily.
# •	Validate domain values after binding.
# •	Return a structured transaction record.

def register_transaction(transaction_id, amount, /, transaction_type, *, currency, status="PENDING"):
    return {
        "transaction_id": transaction_id,
        "amount": amount,
        "transaction_type": transaction_type,
        "currency": currency,
        "status": status
    }



# Test Cases 

# TC1
print(register_transaction("TX1", 100, "BUY", currency="INR"))

# TC2
print(register_transaction(
    "TX2", 200,
    transaction_type="SELL",
    currency="USD"
))

# TC3
print(register_transaction(
    "TX3", 300,
    "BUY",
    currency="EUR",
    status="SETTLED"
))


# TC4: transaction_id supplied by keyword
print(register_transaction(
    transaction_id="TX1",
    100,
    "BUY",
    currency="INR"
))

# TC5: amount supplied by keyword
register_transaction(
    "TX1",
    amount=100,
    "BUY",
    currency="INR"
)

# TC6: currency supplied positionally
register_transaction(
    "TX1", 100, "BUY", "INR"
)

# TC7: currency omitted
register_transaction(
    "TX1", 100, "BUY"
)