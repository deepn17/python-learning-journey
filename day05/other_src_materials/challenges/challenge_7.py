# Challenge 7 — List argument unpacking and numeric operations
# Build reusable numeric operations that accept unpacked collections while enforcing operation-specific argument counts and numeric types.
# Business requirements
# •	Validate numeric arguments once in a reusable helper.
# •	Reject bool and non-numeric values.
# •	Implement sum and product with exactly two values and average with exactly three values, matching the recorded exercise contract.
# •	Allow a wrapper to unpack a collection into the selected operation.
#Technical requirements
# •	Implement `validate_numeric_args(*args)`.
# •	Implement `calculate_sum(*args)`, `calculate_product(*args)`, and `calculate_average(*args)`.
# •	Wrong argument counts raise ValueError.
# •	Invalid numeric types raise TypeError.
# •	Implement `execute_calculation(operation, values)` and unpack values when invoking the operation.
# •	Include `calculate_any_sum(*args)` as the flexible sum extension.

def validate_numeric_args(*args):
    for value in args:
        if not isinstance(value, (int, float)) or isinstance(value, (bool)):
            raise TypeError(f"Incorrect data type provide for '{value}'. Data Type expected is Numbers only.")


def calculate_sum(*args):
    if len(args) != 2:
        raise ValueError("Exactly two arguments required.")

    validate_numeric_args(*args)
    
    return sum(args)


def calculate_product(*args):
    if len(args) != 2:
        raise ValueError("Exactly two arguments required.")

    validate_numeric_args(*args)

    return args[0] * args[1]


def calculate_average(*args):
    if len(args) != 3:
        raise ValueError("Exactly three arguments required.")

    validate_numeric_args(*args)

    return sum(args) / len(args)

def execute_calculation(operation, values):
    if not callable(operation):
        raise TypeError("Operation must be callable")
    return operation(*values)

def calculate_any_sum(*args):
    validate_numeric_args(*args)
    return sum(args)


# Positive Test cases
# calculate_sum(2, 3)	5
# calculate_sum(1.5, 2.5)	4.0
# calculate_product(4, 5)	20
# calculate_average(3, 6, 9)	6.0
# calculate_average(1, 2, 3)	2.0
# execute_calculation(calculate_sum, (4, 6))	10
# execute_calculation(calculate_product, [4, 5])	20
# calculate_any_sum()	0
# calculate_any_sum(1, 2, 3, 4)	10
# calculate_any_sum(1.5, 2.5)	4.0


# Negative Test cases

# calculate_sum(2)	ValueError
# calculate_sum(1, 2, 3)	ValueError
# calculate_product(2)	ValueError
# calculate_product(2, 3, 4)	ValueError
# calculate_average(1, 2)	ValueError
# calculate_average(1, 2, 3, 4)	ValueError
# calculate_sum(True, 2)	TypeError
# calculate_sum(2, "3")	TypeError
# calculate_product(2, False)	TypeError
# calculate_average(1, None, 3)	TypeError
# calculate_any_sum(True, 2)	TypeError
# calculate_any_sum(1, "2")	TypeError
# execute_calculation("add", (2, 3))	TypeError
# execute_calculation(calculate_sum, (2,))	ValueError


# A sample exercise for value unpacking.
def process(a, b, c):
    return a + b + c

values = [10, 20, 30]

# print(process(values))
print(process(*values))
