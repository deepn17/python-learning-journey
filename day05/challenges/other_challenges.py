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