# Example: Simple if
age = int(input("Enter your age: "))

if age >= 18:
    print("You are an adult.")
    print("You can vote!")

print("This line always runs — it's outside the if block.")

# Example: Even or Odd
number = int(input("Enter a number: "))

if number % 2 == 0:
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")

# Example: The Ternary Expression — A One-Line if/else
# long form
score = 60
if score >= 50:
    print("pass")
else:
    print("fail")

# Ternary (one-liner)
result = "pass" if score >= 50 else "fail"
print(result)

"""
The pattern is: value_if_true if condition else value_if_false. Use it sparingly — only when it improves readability, not when the logic is complex.
"""

# Example: if / elif / else
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")

"""
If you reversed the order, you'd get the wrong result.Rule of thumb: when using elif chains, order conditions from most specific to least specific, or from highest threshold to lowest.
"""

# Example: elif vs. Multiple if Statements
# Using elif — only ONE block runs
x = 10
if x > 5:
    print("A")   # Runs
elif x > 3:
    print("B")   # Skipped

# Using separate ifs — MULTIPLE blocks can run
if x > 5:
    print("A")   # Runs
if x > 3:
    print("B")   # Also runs!

"""
Use elif when the conditions are mutually exclusive (only one should match). Use separate if statements when multiple conditions can be true simultaneously and you want to handle each independently.
"""

# Example: The input validator
choice = input("Continue? (y/n): ").lower().strip()

if choice == 'y' or choice == 'yes':
    print("Continuing....")
elif choice == 'n' or choice == 'no':
    print("Existing....")
else:
    print("Invalid input. Please enter y or n.")


# Example: The Range Checker
score = float(input("Score (0-100): "))

if 0 <= score <= 100:
    if score >= 90:
        grade = 'A'
    elif score >= 80:
        grade = 'B'
    elif score >= 70:
        grade = 'C'
    elif score >= 60:
        grade = 'D'
    else:
        grade = 'F'
    print(f"Grade: {grade}")
else:
    print("Score must be between 0 and 100.")

# Example: The Menu Dispatcher
balance = 10000
print("2. Deposit")
print("3. Withdraw")
print("4. Exit")

choice = input("Choose an option: ")

if choice == "1":
    print(f"Balance: ₹{balance}")
elif choice == "2":
    amount = float(input("Amount: "))
    balance += amount
elif choice == "3":
    amount = float(input("Amount: "))
    if amount <= balance:
        balance -= amount
    else:
        print("Insufficient find")
elif choice == "4":
    print("Goodbye")


# Example: The Guard Clause
def process_order(order):
    if order is None:
        return "No order provided."
    if not order.items:
        return "Order is empty."
    if order.is_cancelled:
        return "Order was cancelled."

    total = sum(item.price for item in order.items)
    return f"Total: ₹{total:.2f}"


# Example: Number analyzer
user_input = input("Enter an integer: ").strip()

# Guard: check if they actually typed something
if not user_input:
    print("You didn't enter anything.")
else:
    # Try to convert — handle non-numeric input
    if user_input.lstrip("-").isdigit():
        num = int(user_input)

        # sign check
        if num > 0:
            sign = "Positive"
        elif num < 0:
            sign = "Negative"
        else:
            sign = "Zero"

        # parity check
        if num == 0:
            parity = "neither even or odd"
        elif num % 2 == 0:
            parity = "Even"
        else:
            parity = "Odd"

        # Magnitude check with chaining
        if num == 0:
            magnitude = ""
        elif 0 < abs(num) <= 10:
            magnitude = "small"
        elif 10 < abs(num) <= 100:
            magnitude = "medium"
        elif 100 < abs(num) <= 1000:
            magnitude = "large"
        else:
            magnitude = "huge"

        # Divisibility checks
        facts = []
        if num != 0 and num % 3 == 0:
            facts.append("divisible by 3")
        if num != 0 and num % 5 == 0:
            facts.append("divisible by 5")
        if num != 0 and num % 7 == 0:
            facts.append("divisible by 7")

        # Output
        print(f"\n{num} is {magnitude} {sign} number and is {parity}")
        if facts:
            print(f"It is also {' and '.join(facts)}")
    else:
        print("That's not a valid integer.") 