"""
Data Pipeline — Putting It All Together
===========================================================
A complete program that uses functions to build a small data
processing pipeline.

It processes a list of raw sales records through a pipeline of
functions: clean → validate → transform → aggregate → report.

"""
# raw data
raw_sales = [
    {"product": "  Laptop ", "quantity": "2", "price": "999.99"},
    {"product": "MOUSE",    "quantity": "5", "price": "19.99"},
    {"product": " keyboard ", "quantity": "3", "price": "49.50"},
    {"product": "Monitor",  "quantity": "1", "price": "199.00"},
    {"product": "laptop",   "quantity": "1", "price": "999.99"},
    {"product": "  mouse ", "quantity": "10", "price": "19.99"},
    {"product": "Headphones", "quantity": "2", "price": "89.99"},
]

# cleaning function - Transformation
def clean_product_name(name: str) -> str:
    """strip whitespace and title-case a product name"""
    return name.strip().title()

def to_int(value: str) -> int:
    """convert a string to int, defaulting 0 on failure"""
    try:
        return int(value)
    except ValueError:
        return 0

def to_float(value: str) -> float:
    """convert a string to float, defaulting 0.0 on failure"""
    try:
        return float(value)
    except ValueError:
        return 0.0

def clean_record(record: dict) -> dict:
    """Clean a single raw record in to a normalized dict"""
    return {
        "product": clean_product_name(record["product"]),
        "quantity": to_int(record["quantity"]),
        "price": to_float(record["price"])

    }

# transforming functions - adding new fields to record dictionary

def add_total(record: dict) -> dict:
    """Add a 'total' field (quantity * price) to a record"""
    record["total"] = round(record["quantity"] * record["price"], 2)
    return record

def is_valid(record: dict) -> bool:
    """A record is valid if quantity > 0 and price > 0"""
    return record["quantity"] > 0 and record["price"] > 0


# aggregate functions
def aggregate_by_product(records: list) -> list:
    """Sum quantity and total per product name"""
    result = {}
    for r in records:
        product = r["product"]
        if product not in result:
            result[product] = {"quantity": 0, "total": 0}
        result[product]["quantity"] += r["quantity"]
        result[product]["total"] += r["total"]
    return result

def summarize(records: list) -> dict:
    """Return overall stats for a list of records."""
    if not records:
        return {"count": 0, "revenue": 0}
    return {
        "count": len(records),
        "revenue": round(sum(r["total"] for r in records), 2)
    }


# SECTION: The pipeline (composition!)
def run_pipeline(raw: list) -> dict:
    """
    Run the full pipeline: clean → transform → filter → aggregate.

    Returns a dict with the cleaned records and the summary.
    """
    # 1. Clean every record
    cleaned = [clean_record(r) for r in raw]

    # 2. Add the total field
    with_totals = [add_total(r) for r in cleaned]

    # 3. Filter out invalid records
    valid = [r for r in with_totals if is_valid(r)]

    # 4. Aggregate
    by_product = aggregate_by_product(valid)
    overall = summarize(valid)

    return {
        "records": valid,
        "by_product": by_product,
        "overall": overall,
    }


# SECTION: Reporting
def print_report(result: dict) -> None:
    """Print a human-readable report from the pipeline result."""
    print("\n--- Cleaned Records ---")
    for r in result["records"]:
        print(f"  {r['product']:<12} x{r['quantity']:<3} "
              f"@ ₹{r['price']:<8.2f} = ₹{r['total']:.2f}")

    print("\n--- By Product ---")
    for product, data in result["by_product"].items():
        print(f"  {product:<12} qty={data['quantity']:<3} "
              f"total=₹{data['total']:.2f}")

    print("\n--- Overall ---")
    print(f"  Records: {result['overall']['count']}")
    print(f"  Revenue: ₹{result['overall']['revenue']:.2f}")


# SECTION : Main
def main():
    result = run_pipeline(raw_sales)
    print_report(result)

if __name__ == "__main__":
    main()
