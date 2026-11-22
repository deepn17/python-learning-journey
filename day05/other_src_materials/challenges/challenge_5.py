# Challenge 5 — Configuration validation
# Validate a flexible configuration payload against an allow-list so that unsupported keys, invalid enumerations, and unsafe numeric settings are rejected before the application uses them.
# Business requirements
# •	Accept configuration entries as keyword arguments.
# •	Allow only approved keys.
# •	Restrict currency to INR, USD, or EUR.
# •	Restrict environment to DEV, UAT, or PROD.
# •	Require retry_count to be a positive integer and max_limit to be a positive number.

# Platform-level technical requirements
# •	Implement `validate_config(**kwargs)`.
# •	Use `ALLOWED_KEYS` and `ALLOWED_VALUES` as central policy definitions.
# •	Reject unknown keys with ValueError.
# •	Validate enumerated values.
# •	Explicitly reject bool for numeric fields.
# •	Return a normalized/copy result; empty configuration returns an empty dictionary.

import math
ALLOWED_KEYS = {
    "currency", "max_limit", "retry_count", "timeout", "environment"
}

ALLOWED_VALUES = {
    "currency": {"INR", "USD", "EUR"},
    "environment": {"DEV", "PROD", "UAT"}
}

def validate_config(**kwargs):

    given_configurations = kwargs

    if not given_configurations:
        return {}

    configurations = given_configurations.copy()



    for key, value in configurations.items():
        if key not in ALLOWED_KEYS:
            raise ValueError(f"'{key}' is not permissable")

        if key in ALLOWED_VALUES:
            if value not in ALLOWED_VALUES[key]:
                raise ValueError(f"Invalid Configuration Value for {key}: '{value}'")

        if key == 'retry_count':
            if not isinstance(value, (int)) or isinstance(value, (bool)):
                raise TypeError(f"'{key}' must be a number data type")
            
            if value < 1:
                raise ValueError(f"'{key}' must be a positive integer.")

        if key == 'max_limit':
            if not isinstance(value, (int, float)) or isinstance(value, (bool)):
                raise TypeError(f"'{key} must be a number data type'.")

            if not math.isfinite(value):
                raise ValueError(f"'{key}' must be a finite number.")
            
            if value <= 0:
                raise ValueError(f"'{key}' must be a positive number.")


    return configurations


# Test cases

# TC - 1 
print(validate_config())

# TC - 2 
print(validate_config(currency="INR"))

# TC - 3 
print(validate_config(currency="USD"))

# TC - 4 
print(validate_config(currency="EUR"))

# TC - 5
print(validate_config(environment="DEV"))

# TC - 6
print(validate_config(environment="UAT"))

# TC - 7
print(validate_config(environment="PROD"))

# TC - 8
print(validate_config(retry_count=1))

# TC - 9
print(validate_config(retry_count=3))

# TC - 10
print(validate_config(max_limit=100))

# TC - 11
print(validate_config(max_limit=100.5))	

# TC - 12
print(validate_config(max_limit=0.5))

# TC - 13
print(validate_config(timeout=5))

# TC - 14
result = validate_config(
            currency="INR",
            environment="DEV",
            retry_count=3,
            max_limit=100.5,
            timeout=5
        )

print(result)

# Negative Test Cases
# TC - 1 
# print(validate_config(unknown_option=True))

# TC - 2
# print(validate_config(currency="GBP"))

# TC - 3
# print(validate_config(environment="production"))

# TC - 4
# print(validate_config(retry_count="3"))

# TC - 5
# print(validate_config(retry_count=1.5))

# TC List of Negatives
# - validate_config(retry_count=True)
# - validate_config(retry_count=0)
# - validate_config(retry_count=-1)
# - validate_config(max_limit="100")
# - validate_config(max_limit=True)
# - validate_config(max_limit=0)
# - validate_config(max_limit=-10)

    # -----------------------------
    # INFINITY AND NAN TEST CASES
    # -----------------------------

# - validate_config(max_limit=float("inf"))
# - validate_config(max_limit=float("-inf"))
# - validate_config(max_limit=float("nan"))


