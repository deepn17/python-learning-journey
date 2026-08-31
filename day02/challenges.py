# ============================================================
# CHALLENGE 1: Leap Year Checker
# ============================================================
"""
Ask for a year and print whether it's a leap year.

Leap year rules:
   - Divisible by 4 → leap year
   - BUT if divisible by 100 → NOT a leap year
   - UNLESS also divisible by 400 → leap year again

Examples: 2000 is a leap year | 1900 is not a leap year | 
          2024 is a leap year | 2023 is not a leap year
"""

year = int(input("Enter a year: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year} is a leap year")
        else:
            print(f"{year} is not a leap year")
    else:
        print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year.")

"""
The above leap year logic can be written in many different ways, but i chose the nested conditionals method.
"""

# ============================================================
# CHALLENGE 2: Simple Calculator
# ============================================================
# Ask for two numbers and an operator (+, -, *, /).
# Perform the operation and print the result.
# Handle division by zero gracefully.
#
# Concepts: if/elif chains, error handling
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
action = input("Enter the action you want to perform (+, -, *, /): ")

if action == "+":
    print(f"{num1 + num2:.3f}")
elif action == "-":
    print(f"{num1 - num2:.3f}")
elif action == "*":
    print(f"{num1 * num2:.3f}")
elif action == "/":
    if num2 == 0:
        print("Divisor can't be zero.")
    else:
        print(f"{num1 / num2:.3f}")
else:
    print("Please select from the defined actionable parameters.")

# ============================================================
# CHALLENGE 3: Password Strength Checker
# ============================================================
# Ask for a password and rate it as "Weak", "Medium", or "Strong".
#
# Weak:   fewer than 8 characters
# Medium: 8+ characters, but only letters OR only letters+digits
# Strong: 8+ characters, has letters AND digits AND special chars
#
# Hint: use .isalpha(), .isdigit(), .isalnum(), len()

password = input("Enter your password: ")

if password:
    if len(password) < 8:
        print("Weak Password")
    elif password.isalnum():
        print("Strength is Medium.")  
    else:
        print("Strong Password.")
else:
    print("Password cannot be blank.")

# ============================================================
# CHALLENGE 4: Rock Paper Scissors
# ============================================================
# Two players enter their moves (rock/paper/scissors).
# The program decides who wins (or if it's a draw).
#
# Rules: rock beats scissors, scissors beats paper, paper beats rock
#
# Concepts: nested conditionals, string comparison

valid_moves = ('rock', 'paper', 'scissors')

player1 = input("Player1 Moves: ").lower()
player2 = input("Player2 Moves: ").lower()

if player1 not in valid_moves:
    print('Invalid move for player1')

elif player2 not in valid_moves:
    print('Invalid move for player2')

elif player1 == player2:
    print("It's a draw")

else:
    if player1 == "rock" and player2 == "scissors":
        print("Player1 Wins")
    elif player1 == "scissors" and player2 == "paper":
        print("Player1 Wins")
    elif player1 == "paper" and player2 == "rock":
        print("Player1 Wins")
    else:
        print("Player2 Wins")


# ============================================================
# CHALLENGE 5: Electricity Bill Calculator
# ============================================================
# Calculate electricity bill based on units consumed:
#   First 100 units:  ₹5 per unit
#   Next 100 units:   ₹7 per unit
#   Beyond 200 units:  ₹10 per unit
#
# Example: 250 units → (100×5) + (100×7) + (50×10) = ₹1,700
#
# Concepts: multi-range if/elif, arithmetic

units_consumed = int(input("Enter the units consumed: "))

if units_consumed < 0:
    print("Units cannot be negative.")
elif 0 <= units_consumed <= 100:
    print(f"Bill is: {units_consumed * 5}")
elif 100 < units_consumed <= 200:
    print(f"Bill is: {(100 * 5) + ((units_consumed - 100) * 7)}")
else:
    print(f"Bill is: {(100 * 5) + (100 * 7) + ((units_consumed-200) * 10)}")

# ============================================================
# CHALLENGE 6: Day of the Week
# ============================================================
# Ask for a number 1-7 and print the corresponding day.
#   1 = Monday, 2 = Tuesday, ..., 7 = Sunday
# Handle invalid input (numbers outside 1-7, non-numeric input).
#
# Concepts: if/elif chain, input validation

day_num = input("Enter a number from (1 - 7) corresponding to the days in a week")

if not day_num.isdigit():
    print("Please enter a number from (1 - 7) ")
else:
    day_num = int(day_num)

    if day_num < 1 or day_num > 7:
        print("Please enter a number from (1 - 7)")
    elif day_num == 1:
        print("It's Monday.")
    elif day_num == 2:
        print("It's Tuesday.")
    elif day_num == 3:
        print("It's Wednesday.")
    elif day_num == 4:
        print("It's Thursday.")
    elif day_num == 5:
        print("It's Friday.")
    elif day_num == 6:
        print("It's Saturday.")
    else:
        print("It's Sunday.")