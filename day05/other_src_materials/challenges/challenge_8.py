# Challenge 8 — Function introspection with inspect.signature
# Build a metadata inspector that describes a function’s public calling interface without executing the function.
# Business requirements
# •	Report the function name and documentation string.
# •	Report parameter names in declaration order.
# •	Report each parameter kind and default.
# •	Separate required and optional parameters.
# •	Handle functions with no docstring and functions using all parameter kinds.

# Technical requirements
# •	Implement `inspect_function(func)` using `inspect.signature(func)`.
# •	Extract POSITIONAL_ONLY, POSITIONAL_OR_KEYWORD, VAR_POSITIONAL, KEYWORD_ONLY, and VAR_KEYWORD.
# •	Return a consistent dictionary schema.
# •	Do not hardcode parameter names or invoke the inspected function.

import inspect

def inspect_function(func):
    signature = inspect.signature(func)
    parameters = signature.parameters

    parameter_names = []
    parameter_kinds = {}
    required_parameters = []
    optional_parameters = []
    default_values = {}
    function_name = func.__name__
    documentation = func.__doc__

    for name, parameter in parameters.items():
        parameter_names.append(name)
        parameter_kinds[name] = parameter.kind.name
        if parameter.kind in (inspect.Parameter.VAR_POSITIONAL, inspect.Parameter.VAR_KEYWORD):
            optional_parameters.append(name)
        elif parameter.default is inspect.Parameter.empty:
            required_parameters.append(name)
        else:
            optional_parameters.append(name)
            default_values[name] = parameter.default


    return {
        "function_name": function_name,
        "parameter_names": parameter_names,
        "parameter_kinds": parameter_kinds,
        "required_parameters": required_parameters,
        "optional_parameters": optional_parameters,
        "default_values": default_values,
        "documentation": documentation
    }

# Exercise

def register_transaction(transaction_id, amount, /, transaction_type, *, currency, status="PENDING"):
    return {
        "transaction_id": transaction_id,
        "amount": amount,
        "transaction_type": transaction_type,
        "currency": currency,
        "status": status
    }

# TC for coding
print(inspect_function(register_transaction))

# Sample Test Cases 
def simple_function(a, b):
    pass

def default_function(a, b=10, c=20):
    pass

def mixed_function(a, b, /, c=10, *args, d, e=20, **kwargs):
    pass

def flexible_function(*args, **kwargs):
    pass

def no_parameter_function():
    pass

def documented_function(amount, currency="INR"):
    """Calculate a transaction amount in the specified currency."""
    pass


# Positive test cases 
# inspect_function(simple_function)	- Both parameters are required
# inspect_function(default_function) - a required; b and c optional; defaults recorded
# inspect_function(mixed_function) - Correctly identifies all five parameter kinds
# inspect_function(flexible_function) - Both args and kwargs identified as optional
# inspect_function(no_parameter_function) - Empty parameter collections
# inspect_function(documented_function) - Function name and documentation returned correctly


# Negative test cases

# inspect_function(100)	AttributeError
# inspect_function("calculate")	AttributeError
# inspect_function(None)	AttributeError
# inspect_function([])	AttributeError

# Edge cases
# Function with only positional-only parameters	- All identified as POSITIONAL_ONLY
# Function with only keyword-only parameters - All identified as KEYWORD_ONLY
# Function with multiple default values	- Every default captured
# Function with no docstring - Documentation returned as None
# Function with a docstring	- Documentation returned correctly
# Function with all five parameter kinds - Every parameter classified correctly