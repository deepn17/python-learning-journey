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

# % is the MODULO operator — gives the remainder after division.
# number % 2 is 0 for even numbers, 1 for odd numbers.

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

# COMPARISON CHAINING

"""
In most languages:  if (x > 0 && x < 100)
In Python:          if 0 < x < 100

Python evaluates a < b < c as (a < b) and (b < c)
The middle expression is evaluated ONLY ONCE.
"""
# example 
num1 = int(input("Enter a number: "))

if 0 < num1 < 100:
    print(f"{num1} is between 0 and 100(exclusive)")
elif num1 == 0 or num1 == 100:
    print(f"{num1} is exactly on the boundary.")
else:
    print(f"{num1} is outside the range.")

print("\nValid chaining examples:")
print("  0 <= score <= 100     # score between 0 and 100 inclusive")
print("  a == b == c           # all three are equal")
print("  0 < x <= 10           # x strictly > 0, up to 10")
print("  1 < x < y < z < 100   # all four in ascending order")


# NESTED CONDITIONALS — DECISIONS INSIDE DECISIONS
# Example: odd or even with positive and negative check
n = int(input("Enter an integer: "))

if n > 0:
    if n % 2 == 0:
        print(f"{n} is positive and even.")
    else:
        print(f"{n} is positive and odd.")
elif n < 0:
    if n % 2 == 0:
        print(f"{n} is negative and even.")
    else:
        print(f"{n} is negative and odd.")
else:
    print("The number is zero.")

# TRUTHINESS AND FALSINESS
"""
Every value in Python has an implicit boolean value.
FALSY values (evaluate to False):
False, None, 0, 0.0, "" (empty string),
[] (empty list), {} (empty dict), () (empty tuple)

TRUTHY values: EVERYTHING ELSE
"""
# example:
name = input("Enter your name: ").strip()

if name:
    print(f"Hello, {name}!")
else:
    print("You didn't enter a name.")

"""
This is idiomatic Python:
if name:         is preferred over    if name != "":
if items:        is preferred over    if len(items) > 0:
"""

# Example: Logical operators
age = int(input("Age: "))
has_ticket = input("Do you have a ticket? (yes/no): ").lower() == "yes"
is_vip = input("Are you a VIP? (yes/no): ").lower() == "yes"

if (age >= 18 and has_ticket) or is_vip:
    print("You can enter the show.")
else:
    print("Sorry!, you cannot enter")

"""
SHORT-CIRCUIT EVALUATION:
Python evaluates left to right and STOPS as soon as it knows the answer.
False and anything()  →  anything() NEVER runs
True or anything()    →  anything() NEVER runs
"""

# Example: 
color = input("Enter a color: ").lower()

"""
WRONG — this is ALWAYS True!
if color == "red" or "blue":
Python sees: (color == "red") or ("blue")
"blue" is a non-empty string → always truthy!
"""
# CORRECT:
if color == "red" or color == "blue":
    print("That's a primary color.")
# BETTER:
elif color in ("red", "blue", "yellow"):
    print("That's a primary color (using 'in').")
else:
    print("Not a primary color.")

# Example: THE in AND not in OPERATORS

char = input("Enter a single character: ").lower()

if len(char) == 1:
    if char in 'aeiou':
        print(f"'{char}' is a vowel.")
    elif char.isalpha():
        print(f"'{char}' is a consonant.")
    else:
        print(f"'{char}' is not a letter")
else:
    print("Please enter exactly one character.")

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
user_input = input("Enter a positive number: ").strip()

if not user_input:                      # Guard 1: empty input
    print("You didn't enter anything.")
elif not user_input.lstrip("-").isdigit():  # Guard 2: not a number
    print("That's not a valid integer.")
elif int(user_input) <= 0:              # Guard 3: not positive
    print("Number must be positive.")
else:
    num = int(user_input)
    print(f"Thank you! You entered {num}.")


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