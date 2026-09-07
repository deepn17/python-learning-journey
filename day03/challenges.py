# CHALLENGE 1: Sum of Numbers
# Ask for a number N and print the sum of all numbers 1 to N.
# EXAMPLE:
# Enter N: 5
# Sum of 1 to 5 = 15

n = int(input("Enter the number: "))

total = 0

for i in range(1, n + 1):
    total = total + i

print(total)

# CHALLENGE 2: Factorial Calculator
# GOAL: Ask for N and print N! (N factorial).
#  N! = N × (N-1) × ... × 2 × 1
# HINTS: accumulator starting at 1 (not 0!), multiply each I
# EXAMPLE:
#   Enter N: 5
#   5! = 120

factorial = 1

for i in range(1, n + 1):
    factorial = factorial * i

print(factorial)

# CHALLENGE 3: Multiplication Table
# GOAL: Ask for a number and print its table from 1 to 10.
# HINTS: for i in range(1, 11), f-string for formatting
# EXAMPLE:
#   Enter a number: 7
#   7 × 1 = 7
#   7 × 2 = 14
#   ...
#   7 × 10 = 70

for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")

# CHALLENGE 4: Guess the Number
#GOAL: Pick a secret number (e.g. 42). Let the user guess until
#correct. Give hints "Too high" / "Too low". Count attempts.
# EXAMPLE:
#   Guess: 50
#   Too high!
#   Guess: 30
#   Too low!
#   Guess: 42
#   Correct! It took 3 attempts.

import random
secret_num = random.randint(1, 101)

attempts = 0
while True:
    guess = input("Enter your guess a number between (1 - 100): ")
    if not guess.isdigit():
        print("Not a number.Try again.")
        continue
    guess = int(guess)

    if guess < 1 or guess > 100:
        print("Out of range! Guess between 1 and 100.")
        continue

    attempts = attempts + 1

    if guess > secret_num:
        print("Your guess is too high.")
    elif guess < secret_num:
        print(f" Your guess is too low")
    else:
        print(f"Your guess is correct. You got it in {attempts} attempts.")
        break

# CHALLENGE 5: Fibonacci Sequence
# GOAL: Print the first N Fibonacci numbers.
#       Sequence: 0, 1, 1, 2, 3, 5, 8, 13, ...
#       Each number is the sum of the two before it.

a, b = 0, 1

for i in range(n):
    print(a, end=" ")
    a, b = b, a + b

# CHALLENGE 6: Count Vowels
# GOAL: Ask for a string and count how many vowels (a, e, i, o, u)
#       it contains (case-insensitive).
# HINTS: loop over the string, use `in "aeiou"`, accumulator count
#
# EXAMPLE:
#   Enter text: Hello World
#   Vowels: 3
#
# Concepts: for loop, membership (in), accumulator

vowels = "aeiou"

text = input("\nEnter the text here: ").lower()
vowel_cnt = 0
for vowel in text:
    if vowel in vowels:
        vowel_cnt += 1
print(vowel_cnt)




