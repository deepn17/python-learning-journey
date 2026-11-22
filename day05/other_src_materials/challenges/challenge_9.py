# Challenge 9 — Validate function calls with signature binding
# Validate whether a proposed set of positional and keyword arguments can legally call a function, without actually executing that function.

# Business requirements
# •	Accept a function plus candidate args and kwargs.
# •	Return whether the call is valid.
# •	When valid, expose the bound argument mapping.
# •	When invalid, return a useful error description.
# •	Apply defaults only after binding succeeds.

# Technical requirements
# •	Implement `validate_function_call(func, *args, **kwargs)`.
# •	Use `inspect.signature(func)` and `signature.bind(*args, **kwargs)`.
# •	Catch TypeError from binding and report it in the result.
# •	Call `bound.apply_defaults()` only after successful binding.
# •	Return a consistent dictionary containing function_name, is_valid, arguments, and error.

import inspect
def validate_function_call(func, *args, **kwargs):

    signature = inspect.signature(func)
    try:
        bound = signature.bind(*args, **kwargs)
        bound.apply_defaults()
    except TypeError as error:
        return {
            "function_name": func.__name__,
            "is_valid": False,
            "arguments": None,
            "error": str(error)
        }

    return {
            "function_name": func.__name__,
            "is_valid": True,
            "arguments": dict(bound.arguments),
            "error": None
        }

# During Coding test cases
def process_request(request_id, /, action, **options):
    pass

def dangerous_operation(name):
    print("FUNCTION EXECUTED!")
    return name

print(validate_function_call(process_request))
print(validate_function_call(dangerous_operation))
print(validate_function_call(dangerous_operation, "John"))


# Sample functions for Testing

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

# Positive Test Cases
# validate_function_call(simple_function, 10, 20)	
# validate_function_call(simple_function, 10, b=20)	
# validate_function_call(default_function, 5)	
# validate_function_call(default_function, 5, 15)	
# validate_function_call(default_function, 5, c=30)	
# validate_function_call(default_function, a=5, b=15, c=25)	
# validate_function_call(mixed_function, 1, 2, d=40)
# validate_function_call(mixed_function, 1, 2, 3, 4, 5, d=40, x=50)	
# validate_function_call(flexible_function, 1, 2, x=10, y=20)
# validate_function_call(no_parameter_function)

# Negative test cases
# validate_function_call(simple_function, 10)
# validate_function_call(simple_function, 10, 20, 30)
# validate_function_call(simple_function, 10, a=20)
# validate_function_call(simple_function, a=10)
# validate_function_call(simple_function, 10, 20, x=30)
# validate_function_call(mixed_function, a=1, b=2, d=30)
# validate_function_call(mixed_function, 1, 2, 3)
# validate_function_call(mixed_function, 1, 2, d=30, d=40)
# validate_function_call(no_parameter_function, 10)
# validate_function_call(no_parameter_function, x=10)

# Additional edge cases
# validate_function_call(default_function, 5, 15, 25)
# validate_function_call(default_function, 5, b=None, c=0)
# validate_function_call(flexible_function)
# validate_function_call(mixed_function, 1, 2, d=None)
# validate_function_call(mixed_function, 1, 2, 3, 4, 5, 6, d=7, e=8, x=9, y=10)