# Challenge 10 — Function composition with compose()
# Create a reusable function that combines multiple functions into one pipeline, applying them from right to left and returning the final result.

# Business requirements
# •	Accept zero or more functions.
# •	Return a callable composed function.
# •	Apply the rightmost function first, then move left.
# •	If no functions are supplied, behave as the identity function.
# •	Reject non-callable inputs and allow execution exceptions to propagate.

# Technical requirements
# •	Implement `compose(*funcs)`.
# •	Validate every supplied object with callable().
# •	Return an inner function that accepts arbitrary positional and keyword arguments for the rightmost function.
# •	Apply remaining functions to the prior result.
# •	Preserve exception propagation and stop when a stage fails.

def compose(*funcs):

    # STEP 1: Validate that every supplied object is callable.
    for func in funcs:
        if not callable(func):
            raise TypeError("Not a Callable Operation")

    # STEP 2: Define the composed function.
    # It accepts arbitrary positional and keyword arguments.
    def composed(*args, **kwargs):

        # STEP 3: Handle the identity case.
        if not funcs:
            if len(args) == 1 and not kwargs:
                return args[0]
            if not args and len(kwargs) == 1:
                return next(iter(kwargs.values()))
            if not args and not kwargs:
                return None
            return args, kwargs

        # STEP 4: Execute the rightmost function first.
        result = funcs[-1](*args, **kwargs)

        # STEP 5: Pass the result through the remaining functions,
        # moving from right to left.
        for func in reversed(funcs[:-1]):
            result = func(result)

        # STEP 6: Return the final pipeline result.
        return result

    # STEP 7: Return the composed callable.
    return composed



# Test cases



# ============================================================
# CHALLENGE 10 — FUNCTION COMPOSITION TEST SUITE
# ============================================================

# STEP 1: Import required module
import unittest


# STEP 2: Define functions used by the test suite

def add_one(x):
    return x + 1


def double(x):
    return x * 2


def square(x):
    return x ** 2


def subtract_ten(x):
    return x - 10


def calculate_amount(amount, *, currency):
    return f"{currency} {amount}"


def divide_by_zero(x):
    return x / 0


def fail_processing(x):
    raise RuntimeError("Processing system unavailable")


# STEP 3: Define execution-tracking functions

execution_log = []


def stage_one(x):
    execution_log.append("stage_one")
    return x + 1


def stage_two(x):
    execution_log.append("stage_two")
    return x * 2


def stage_three(x):
    execution_log.append("stage_three")
    return x - 3


# STEP 4: Define failure-tracking functions

failure_log = []


def successful_stage(x):
    failure_log.append("successful_stage")
    return x + 1


def failing_stage(x):
    failure_log.append("failing_stage")
    raise ValueError("Invalid transaction")


def unreachable_stage(x):
    failure_log.append("unreachable_stage")
    return x * 2


# STEP 5: Define test class

class TestCompose(unittest.TestCase):

    # --------------------------------------------------------
    # POSITIVE TEST CASES
    # --------------------------------------------------------

    def test_single_function(self):
        pipeline = compose(add_one)
        self.assertEqual(pipeline(5), 6)

    def test_two_functions(self):
        pipeline = compose(double, add_one)
        self.assertEqual(pipeline(5), 12)

    def test_three_functions(self):
        pipeline = compose(add_one, double, square)
        self.assertEqual(pipeline(3), 19)

    def test_four_functions(self):
        pipeline = compose(
            subtract_ten,
            add_one,
            double,
            square
        )
        self.assertEqual(pipeline(3), 9)

    def test_keyword_arguments_to_rightmost_function(self):
        pipeline = compose(add_one, calculate_amount)
        self.assertEqual(
            pipeline(1000, currency="INR"),
            "INR 1001"
        )

    def test_right_to_left_execution_order(self):
        global execution_log
        execution_log = []

        pipeline = compose(stage_one, stage_two, stage_three)
        result = pipeline(10)

        self.assertEqual(result, 15)
        self.assertEqual(
            execution_log,
            ["stage_three", "stage_two", "stage_one"]
        )

    # --------------------------------------------------------
    # NEGATIVE TEST CASES
    # --------------------------------------------------------

    def test_non_callable_integer(self):
        with self.assertRaises(TypeError):
            compose(100)

    def test_non_callable_string(self):
        with self.assertRaises(TypeError):
            compose(add_one, "double")

    def test_non_callable_none(self):
        with self.assertRaises(TypeError):
            compose(add_one, None)

    def test_non_callable_in_middle(self):
        with self.assertRaises(TypeError):
            compose(add_one, 100, square)

    def test_division_by_zero_propagates(self):
        pipeline = compose(add_one, divide_by_zero)

        with self.assertRaises(ZeroDivisionError):
            pipeline(10)

    def test_runtime_error_propagates(self):
        pipeline = compose(add_one, fail_processing)

        with self.assertRaisesRegex(
            RuntimeError,
            "Processing system unavailable"
        ):
            pipeline(1000)

    def test_rightmost_function_receives_arguments(self):
        pipeline = compose(add_one, calculate_amount)

        with self.assertRaises(TypeError):
            pipeline(1000)

    # --------------------------------------------------------
    # EDGE CASES
    # --------------------------------------------------------

    def test_zero_functions_returns_callable(self):
        pipeline = compose()
        self.assertTrue(callable(pipeline))

    def test_identity_function_with_integer(self):
        pipeline = compose()
        self.assertEqual(pipeline(42), 42)

    def test_identity_function_with_zero(self):
        pipeline = compose()
        self.assertEqual(pipeline(0), 0)

    def test_identity_function_with_none(self):
        pipeline = compose()
        self.assertIsNone(pipeline(None))

    def test_identity_function_with_string(self):
        pipeline = compose()
        self.assertEqual(pipeline("BANKING"), "BANKING")

    def test_identity_function_with_list(self):
        data = [100, 200, 300]
        pipeline = compose()

        self.assertIs(pipeline(data), data)

    def test_function_returns_none(self):
        def return_none(x):
            return None

        def accept_none(x):
            return x is None

        pipeline = compose(accept_none, return_none)
        self.assertTrue(pipeline(100))

    # --------------------------------------------------------
    # PIPELINE FAILURE BEHAVIOUR
    # --------------------------------------------------------

    def test_pipeline_stops_after_failure(self):
        global failure_log
        failure_log = []

        pipeline = compose(
            unreachable_stage,
            failing_stage,
            successful_stage
        )

        with self.assertRaises(ValueError):
            pipeline(100)

        self.assertEqual(
            failure_log,
            ["successful_stage", "failing_stage"]
        )

        self.assertNotIn("unreachable_stage", failure_log)


# STEP 6: Execute all tests

if __name__ == "__main__":
    unittest.main(verbosity=2)



# An Example for inner function
def outer():
    def inner():
        return "Hello"

    return inner

result = outer()
print(result)
print(result())
