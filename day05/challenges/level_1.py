# 1. Declare a function add_two_numbers. It takes two parameters and it returns a sum.
def add_two_numbers(num_one, num_two):
    """
    Take 2 numbers and return their sum.

    Args:
        num_one: The first number.
        num_two: The second number.

    return:
        The sum of the two numbers
    """
    return num_one + num_two

print(f"Add two numbers: {add_two_numbers(5, 6)}")

# 2. Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.
def area_of_circle(r, pi = 3.14159):
    """
    calculates the area of circle

    Args:
        r: Radius of the circle
        pi: Pi, defaulted to 3.14159.

    return:
        The area of the circle for which the formula is: PI x r x r
    """
    return pi * r * r

print(f"Area of the circle: {area_of_circle(5):.2f}")

# 3. Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments.
# Check if all the list items are number types. If not do give a reasonable feedback.
def add_all_nums(*numbers):
    """
        Sum an arbitrary number of numeric arguments

        Args:
            *numbers: An arbitrary number of integers or floats.

        return:
           The sum of all the numbers, or an error message if
           a non-numeric argument is provided.
        """
    for number in numbers:
        if not isinstance(number, (int, float)):
            return f"{number} is not a number"
    return sum(numbers)

print(add_all_nums(1, 2, 3, 4, 5))
print(add_all_nums(1, 2, "hello", 4))

# 4. Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32.
# Write a function which converts °C to °F, convert_celsius_to-fahrenheit.
def convert_celsius_to_fahrenheit(celsius):
    """
        Convert Celsius to Fahrenheit.

        Args:
            celsius: Temperature in degrees Celsius.

        Returns:
            Temperature in degrees Fahrenheit.
        """
    return celsius * 9 / 5 + 32

print(convert_celsius_to_fahrenheit(0))
print(convert_celsius_to_fahrenheit(35))

# 5. Write a function called check-season, it takes a month parameter and returns the season:
# Autumn, Winter, Spring or Summer.
def check_season(month):
    """
    Find the season of the year.

    Args:
        month: Month of the year.

    Returns:
        The season based on the month.
    """
    if month.lower() in ["december", "january", "february"]:
        return f"Season is Winter"
    elif month.lower() in ["march", "april", "may"]:
        return f"Season is Spring"
    elif month.lower() in ["june", "july", "august"]:
        return f"Season is Summer"
    elif month.lower() in ["september", "october", "november"]:
        return f"Season is Autumn"
    else:
        return f"Not a valid month"

print(check_season("tres"))
print(check_season("November"))
print(check_season("May"))

# 6. Write a function called calculate_slope which return the slope of a linear equation
def calculate_slope(x1, y1, x2, y2):
    """
    Calculate the slope of the line

    Args:
        x1: x-coordinate of the first point.
        y1: y-coordinate of the first point.
        x2: x-coordinate of the second point.
        y2: y-coordinate of the second point.

    return:
        The slope of the line
    """
    return (y2 - y1) / (x2 - x1)

print(calculate_slope(2, 3, 4, 5))
print(calculate_slope(4, 5, 6, 7))

# 7. Quadratic equation is calculated as follows: ax² + bx + c = 0.
# Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.
def solve_quadratic_eqn(a, b, c):
    """
    Calculate the solution(s) of a quadratic equation.

    The equation is:
        ax² + bx + c = 0

    Args:
        a: Coefficient of x².
        b: Coefficient of x.
        c: Constant.

    Returns:
        The solution(s) of the quadratic equation.
    """
    # calculate the discriminant
    discriminant = b ** 2 - 4 * a * c

    # two real solutions
    if discriminant > 0:
        x1 = (-b + discriminant ** 0.5) / (2 * a)
        x2 = (-b + discriminant ** 0.5) / (2 * a)
        return x1, x2

    # one real solution
    elif discriminant == 0:
        x = -b / (2 * a)
        return x

    # no real solutions
    else:
        return "No real solutions"

print(solve_quadratic_eqn(1, -5, 6))
print(solve_quadratic_eqn(1, -4, 4))
print(solve_quadratic_eqn(1, 2, 5))

# 8. Declare a function named print_list. It takes a list as a parameter
# and it prints out each element of the list.
def print_list(items):
    """
    Print each element of a list.

    Args:
        items: A list containing the elements to print.
        """
    for item in items:
        print(item)

print_list([1, 2, 'Deepak', 4.7])

# 9. Declare a function named reverse_list. It takes an array as a parameter and it
# returns the reverse of the array (use loops).
def reverse_list(items):
    """
    Reverse a list using a loop.

    Args:
        items: A list of elements to be reversed.

    Returns:
        A new list containing the elements in reverse order.
    """
    reversed_items = []

    for i in range(len(items) -1, -1, -1):
        reversed_items.append(items[i])

    return reversed_items

print(reverse_list([1, 2, 3, 4, 5]))
print(reverse_list(["A", "B", "C"]))

# 10. Declare a function named capitalize_list_items. It takes a list as a parameter
# and it returns a capitalized list of items
def capitalize_list_items(items):
    """
    Capitalize string items in a list while leaving non-string items unchanged.

    Args:
        items: A list containing strings or other data types.

    Returns:
        A new list with string items capitalized.
        """

    capitalized_items = []

    for item in items:
        if isinstance(item, str):
            capitalized_items.append(item.capitalize())
        else:
            capitalized_items.append(item)

    return capitalized_items

print(capitalize_list_items(["dracarys", "Mall", "player"]))
print(capitalize_list_items(["dracarys", "Mall", "player", 4.15, 4, True]))

# 11. Declare a function named add_item. It takes a list and an item parameters.
# It returns a list with the item added at the end.
def add_item(items, item):
    """
    Add an item to the end of a list.

    Args:
    items: The list to which the item will be added.
    item: The item to be added to the list.

    Returns:
    The list with the new item added at the end.
    """
    items.append(item)
    return items

food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(add_item(food_stuff, 'Meat'))

numbers = [2, 3, 7, 9]
print(add_item(numbers, 5))

# 12. Declare a function named remove_item. It takes a list and an item parameters.
# It returns a list with the item removed from it.
def remove_item(items, item):
    """
    Remove an item from the list.

    Args:
        items: The list from which the item will be removed.
        item: The item to be removed.

    Returns:
        The list after removal of the item.
    """
    items.remove(item)
    return items

food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(remove_item(food_stuff, 'Mango'))
numbers = [2, 3, 7, 9]
print(remove_item(numbers, 3))

# 13. Declare a function named sum_of_numbers. It takes a number parameter and
# it adds all the numbers in that range.
def sum_of_numbers(n):
    """
    Calculate the sum of numbers from 1 to n.

    Args:
        n: The positive integer up to which the numbers will be summed.

    Returns:
        The sum of all integers from 1 to n.
    """
    total = 0
    for num in range(1, n + 1):
        total += num
    return total

print(sum_of_numbers(5))
print(sum_of_numbers(10))
print(sum_of_numbers(100))

# 14. Declare a function named sum_of_odds. It takes a number parameter and it adds all
# the odd numbers in that range.
def sum_of_odds(n):
    """
    Calculate the sum of odd numbers from 1 to n.

    Args:
        n: The positive integer up to which the numbers will be summed.

    Returns:
        The sum of all odd integers from 1 to n.
    """
    total = 0
    for num in range(1, n + 1):
        if num % 2 != 0:
            total += num

    return total

print(sum_of_odds(5))
print(sum_of_odds(10))
print(sum_of_odds(100))

# 15. Declare a function named sum_of_even. It takes a number parameter and it adds all
# the even numbers in that - range.

def sum_of_even(n):
    """
    Calculate the sum of even numbers from 1 to n.

    Args:
        n: The positive integer up to which the numbers will be summed.

    Returns:
        The sum of all even integers from 1 to n.
    """
    total = 0
    for num in range(1, n + 1):
        if num % 2 == 0:
            total += num

    return total

print(sum_of_even(5))
print(sum_of_even(10))
print(sum_of_even(100))