full_name = "unknown"      # <class 'str'>
age = 33                   # <class 'int'>
height_m = 1.75            # <class 'float'>
is_learning_python = True  # <class 'bool'>
current_job = None      # between jobs - explicitly no value     <class 'NoneType'>

print(type(full_name))
print(type(age))
print(type(height_m))
print(type(is_learning_python))
print(type(current_job))


# Arithmetic Operators
a = 17
b = 5

print(a + b)    # 22    — addition
print(a - b)    # 12    — subtraction
print(a * b)    # 85    — multiplication
print(a / b)    # 3.4   — true division (always returns a float)
print(a // b)   # 3     — floor division (chops off the decimal)
print(a % b)    # 2     — modulus (the remainder after division)
print(a ** b)   # 1419857 — exponentiation (a to the power of b)


# Comparison Operators — Always Return a bool
x = 10
y = 20

print(x == y)   # False
print(x != y)   # True
print(x < y)    # True
print(x > y)    # False
print(x <= 10)  # True
print(x >= 30)  # False


# Comparison Operators — Always Return a bool
age_id = 20
has_id = True

print(age_id >= 18 and has_id)    # True  — both must be True
print(age_id < 18 or has_id)      # True  — at least one must be True
print(not has_id)                 # False — flips True to False and vice versa


# Input and Formatted Output
f_name = input("Enter your name: ")
print(f"Hello, {f_name}")

price = 19.5
print(f"Price: ${price:.2f}")     # Price: $19.50