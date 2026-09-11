print("=" * 50)
print("Shopping List with Budget")
print("=" * 50)

budget = float(input("What's your budget? ₹"))
cart = []
total = 0.0

while True:
    item = input("\nItem name (or 'done'): ").strip()
    if item.lower() == 'done':
        break
    price = float(input(f"Price of {item}: ₹"))
    cart.append((item, price))
    total += price
    print(f"Running total: ₹{total:.2f}")

    if total > budget:
        print("You are over budget.")

print("\n--- Receipt ---")
for item, price in cart:
    print(f"{item:<15} ₹{price:>8.2f}")
print(f"{'TOTAL':<15} ₹{total:>8.2f}")

if total <= budget:
    print(f"Within Budget! (₹{budget - total:.2f} left)")
else:
    print(f"Over budget by ₹{total - budget:.2f}")
