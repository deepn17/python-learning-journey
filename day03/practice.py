# PRACTICE 1: Print Even Numbers
# GOAL: Print all even numbers from 1 to 20.

for i in range(1, 21):
    if i % 2 == 0:
        print(i)

# PRACTICE 2: Reverse a String
# GOAL: Take a string and print it in reverse using a loop.

text = input("Enter your word here: ")

rev_txt = ""

for char in text:
    rev_txt = char + rev_txt

print(rev_txt)

# PRACTICE 3: Countdown Timer
# GOAL: Ask for a number and count down from it to 0, then print
#       "Blast off!"

num = int(input("Enter the countdown number: "))

while num >= 0:
    print(f"Count down to blast off : {num}")
    num -= 1

print("Blast off")

# PRACTICE 4: Sum of Digits
# ============================================================
# GOAL: Take a number and print the sum of its digits.
# EXAMPLE: 1234 → 1+2+3+4 = 10

number = int(input("Enter a series of number: "))

total = 0

num_str = str(number)

for num in num_str:
    total += int(num)

print(total)

# PRACTICE 5: FizzBuzz
# GOAL: Print numbers 1 to 30, but:
#         - Multiples of 3 → "Fizz"
#         - Multiples of 5 → "Buzz"
#         - Multiples of both → "FizzBuzz"
#         - Otherwise → the number
# EXAMPLE: 1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz ...

for i in range(1, 31):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 5 == 0:
        print("Buzz")
    elif i % 3 == 0:
        print("Fizz")
    else:
        print(i)

# PRACTICE 6: Pyramid Pattern
# GOAL: Print a pyramid of stars of height N (ask the user for N).
# HINTS: each row has (N - i) spaces and (2*i - 1) stars
# EXAMPLE for N=4:

height_of_n = int(input("Enter the height of the pyramid you want: "))

for i in range(1, height_of_n + 1):
    spaces = height_of_n - i
    stars = 2 * i - 1

    print(" " * spaces + "*" * stars)