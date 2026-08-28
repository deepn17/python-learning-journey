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