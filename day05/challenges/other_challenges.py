# ============================================================
# CHALLENGE 1: Temperature Converter
# ============================================================
# GOAL: Write two functions: celsius_to_fahrenheit() and
#       fahrenheit_to_celsius(). Then convert a few values.
#
# HINTS: return the result, use the formulas:
#        F = C * 9/5 + 32   and   C = (F - 32) * 5/9
#
# EXAMPLE:
#   0°C = 32.0°F
#   100°C = 212.0°F
#   32°F = 0.0°C
def celsius_to_fahrenheit(celsius):
    return celsius * 9/5 + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

print(f"0°C = {celsius_to_fahrenheit(0)}°F")
print(f"100°C = {celsius_to_fahrenheit(100)}°F")

print(f"32°F = {fahrenheit_to_celsius(32)}°C")
print(f"212°F = {fahrenheit_to_celsius(212)}°C")

# ============================================================
# CHALLENGE 2: Palindrome Checker
# ============================================================
# GOAL: Write a function is_palindrome(text) that returns True if the
#       text reads the same forwards and backwards (ignore case and
#       spaces).
#
# HINTS: normalize the string (lower, remove spaces), compare to reverse
#
# EXAMPLE:
#   is_palindrome("racecar") → True
#   is_palindrome("A man a plan a canal Panama") → True
#   is_palindrome("hello") → False

def is_palindrome(text):
    normarlized_text = text.lower().replace(" ", "")

    reverse_text = normarlized_text[::-1]

    if normarlized_text == reverse_text:
        return True
    else:
        return False

print(is_palindrome("racecar"))
print(is_palindrome("A man a plan a canal Panama"))
print(is_palindrome("hello"))

# ============================================================
# CHALLENGE 3: Factorial
# ============================================================
# GOAL: Write a function factorial(n) that returns n! (n factorial).
#       Do it BOTH iteratively (loop) and recursively (calls itself).
#
# HINTS: iterative → loop from 1 to n; recursive → n * factorial(n-1)
#
# EXAMPLE:
#   factorial(5) → 120
#   factorial(0) → 1

# without recursion
def factorial(n):

    result = 1

    for i in range(1, n+1):
        result = result * i

    return result

print(factorial(5))
print(factorial(0))

# with recursion
def factorial_recursive(n):

    if n == 0 or n == 1:
        return 1

    return n * factorial_recursive(n - 1)

print(factorial_recursive(5))
print(factorial_recursive(0))

# ============================================================
# CHALLENGE 4: Prime Number Checker
# ============================================================
# GOAL: Write a function is_prime(n) that returns True if n is prime.
#
# HINTS: a prime has no divisors other than 1 and itself
#
# EXAMPLE:
#   is_prime(7) → True
#   is_prime(10) → False
#   is_prime(2) → True

def is_prime(n):
    # numbers less than or equal to 1 are not prime
    if n <= 1:
        return False
    # 2 is the only even number that is prime
    if n == 2:
        return True
    # Exclude all other even numbers
    if n % 2 == 0:
        return False
    # check odd factors up to the square root of n
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False

    return True

# ============================================================
# CHALLENGE 6: Aggregation Function
# ============================================================
# GOAL: Write a function stats(numbers) that returns a dict with
#       count, sum, mean, min, and max. Handle the empty-list case.
#
# HINTS: len(), sum(), min(), max(); guard against empty list
#
# EXAMPLE:
#   stats([1, 2, 3, 4, 5])
#   → {"count": 5, "sum": 15, "mean": 3.0, "min": 1, "max": 5}

def stats(numbers):

    if not numbers:
        return {
            "count": 0,
            "sum": 0,
            "mean": None,
            "min": None,
            "max": None
        }

    stats_dict = {
        "count": len(numbers),
        "sum": sum(numbers),
        "mean": sum(numbers) / len(numbers),
        "min": min(numbers),
        "max": max(numbers)
    }

    return stats_dict

# ============================================================
# CHALLENGE 7: Area Calculator
# ============================================================
# GOAL: Write functions area_circle(r), area_rectangle(w, h), and
#       area_triangle(b, h). Use math.pi for the circle.
# HINTS: import math, return the result
# EXAMPLE: area_rectangle(2, 3) → 6

import math

def area_circle(r):
    return math.pi * r * r

def area_rectangle(w, h):
    return w * h

def area_triangle(b, h):
    return (b * h) / 2


print(f"Area of circle: {area_circle(5):.2f}")
print(f"Area of rectangle: {area_rectangle(5, 10):.2f}")
print(f"Area of triangle: {area_triangle(5, 10):.2f}")

# ============================================================
# CHALLENGE 8: Default Parameter
# ============================================================
# GOAL: Write a function apply_discount(price, rate=0.1) that returns
#       the discounted price. Call it with and without the rate.
# HINTS: default parameter, return
# EXAMPLE: apply_discount(100) → 90.0, apply_discount(100, 0.25) → 75.0

def apply_discount(price, rate=0.1):
    discount = price * rate
    discounted_price = price - discount
    return discounted_price

print(f"The discounted rate without the rate {apply_discount(100):.1f}")
print(f"The discounted rate with the rate {apply_discount(100, 0.25):.1f}")


# ============================================================
# CHALLENGE 9: *args Sum
# ============================================================
# GOAL: Write a function sum_all(*args) that returns the sum of all
#       arguments, and returns 0 if called with no arguments.
# HINTS: *args, sum()
# EXAMPLE: sum_all(1, 2, 3) → 6, sum_all() → 0

def sum_all(*args):
    return sum(args)

print(sum_all(1, 2, 3))
print(sum_all())

# ============================================================
# CHALLENGE 10: **kwargs Filter
# ============================================================
# GOAL: Write a function filter_kwargs(**kwargs) that returns a new
#       dict containing only the key-value pairs where the value is
#       a string.
# HINTS: **kwargs, isinstance(value, str)
# EXAMPLE: filter_kwargs(a=1, b="hi", c=3.0, d="yo") → {"b": "hi", "d": "yo"}

def filter_kwargs(**kwargs):

    filtered_dict = {}

    for key, value in kwargs.items():
        if isinstance(value, str):
            filtered_dict[key] = value

    return filtered_dict

print(filter_kwargs(a=1, b="hi", c=3.0, d="yo"))

# ============================================================
# CHALLENGE 11: map/filter/lambda
# ============================================================
# GOAL: Given a list of numbers, use map() to square each, then
#       filter() to keep only those > 10. Use lambdas.
# HINTS: map(lambda...), filter(lambda...), list()
# EXAMPLE: [1, 2, 3, 4, 5] → squares [1,4,9,16,25] → >10 → [16, 25]
numbers = [1, 2, 3, 4, 5]

squares = list(map(lambda x: x**2, numbers))
filtered_numbers = list(filter(lambda x: x>10, squares))

print("Original numbers", numbers)
print("Squared numbers", squares)
print("Numbers greater than 10", filtered_numbers)


# ============================================================
# CHALLENGE 12: Type-Hinted Function
# ============================================================
# GOAL: Write a type-hinted function median(numbers: list[float]) -> float
#       that returns the median (middle value) of a sorted list.
# HINTS: sort a copy, handle even/odd length
# EXAMPLE: median([1, 2, 3, 4, 5]) → 3.0, median([1, 2, 3, 4]) → 2.5

def median(numbers: list[float]) -> float:

    sorted_numbers = sorted(numbers)
    length = len(numbers)

    if length % 2 == 0:
        first = length // 2 - 1
        second = length // 2

        median = (sorted_numbers[first] + sorted_numbers[second]) / 2

        return median
    else:
        median = sorted_numbers[length // 2]

        return median