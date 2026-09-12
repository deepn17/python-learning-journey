print("=" * 50)
print("Number Analyzer")
print("=" * 50)

numbers = []

while True:
    entry = input("Enter a number (or 'done'): ").strip()
    if entry.lower() == 'done':
        break
    if entry.lstrip("-").isdigit():
        numbers.append(int(entry))
    else:
        print("That's not a valid number")

if not numbers:
    print("No numbers entered.")
else:
    evens = [n for n in numbers if n % 2 == 0]
    odd = [n for n in numbers if n % 2 != 0]

    print(f"\nCount:  {len(numbers)}")
    print(f"Sum:  {sum(numbers)}")
    print(f"Average:  {sum(numbers) / len(numbers):.2f}")
    print(f"Min:  {min(numbers)}")
    print(f"Max:  {max(numbers)}")
    print(f"Evens:  {len(evens)}  ({evens})")
    print(f"Odds:  {len(odd)}  ({odd})")
    print(f"Sorted:  {sorted(numbers)}")