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

# 16. Declare a function named evens_and_odds . It takes a positive integer as parameter and it counts number of evens and odds in the number.

def evens_and_odds(num):
    """
    Count the number of even and odd integers from 0 to the given number.

    Args:
        num (int): A positive integer representing the upper limit.

    Returns:
        str: A formatted string containing the count of even and odd numbers.
    """
    even_count = 0
    odd_count = 0

    for i in range(num + 1):
        if i % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    return f"The number of odds are {odd_count}.\nThe number of evens are {even_count}."


print(evens_and_odds(100))

# 17. Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number

def factorial(n):
    """
    Calculate the factorial of a given whole number.

    Args:
        n (int): A non-negative integer whose factorial is to be calculated.

    Returns:
        int: The factorial of the given number.
    """
    result = 1

    for i in range(1, n + 1):
        result *= i

    return result

print(factorial(5)) 
print(factorial(4)) 
print(factorial(0))

# 18. Call your function is_empty, it takes a parameter and it checks if it is empty or not
def is_empty(items = None):
    """
    Check whether the given parameter is empty or falsy.

    Args:
        items: The value to be checked. Defaults to None.

    Returns:
        bool: True if the value is falsy (None, empty collection, 0, False, etc.),
              otherwise False.
    """
    if not items:
        return True
    else:
        return False

print(is_empty())
print(is_empty([]))
print(is_empty(""))
print(is_empty([1, 2, 3]))

# 19. Write different functions which take lists. They should calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviation).
def calulate_mean(numbers):
    """
    Calculates the mean for a given list of numbers
    
    Args:
        items: A list of numbers for which the mean is to be calculated
    
    Returns:
        The mean from the list of given numbers
    """
    return f"Mean of the numbers is: {sum(numbers) / len(numbers)}"

def calculate_median(numbers):
    """
    Calculates the median for a given list of numbers
    
    Args:
        items: A list of numbers for which the median is calculated
    
    Returns:
        The median from the list of given numbers.
    """
    sorted_numbers = sorted(numbers)
    length = len(numbers)

    if length % 2 == 0:
        first_element = sorted_numbers[length // 2 - 1]
        second_element = sorted_numbers[length // 2]
        median = (first_element + second_element) / 2

        return median
    else:
        median = sorted_numbers[length // 2]

        return median

def calculate_mode(numbers):
    """
    Calculates the mode for a given list of numbers
        
    Args:
        items: A list of numbers for which the mode is calculated
        
    Returns:
        The mode from the list of given numbers.
    """
    max_count = 0
    modes = []

    for n in numbers:
        count = numbers.count(n)

        if count > max_count:
            max_count = count
            modes = [n]
        elif count == max_count and n not in modes:
            modes.append(n)

    if max_count == 1:
        return "No Mode Exists"

    return modes


def calculate_range(numbers):
    """
    Calculates the range for a given list of numbers. Max number in range - Min number in range
        
    Args:
        numbers: A list of numbers for which the range is calculated
        
    Returns:
        The range for the list of given numbers.
    """
    max_num = numbers[0]
    min_num = numbers[0]

    for n in numbers:
        if n > max_num:
            max_num = n
        if n < min_num:
            min_num = n

    range_numbers = max_num - min_num

    return range_numbers


def calculated_range(numbers):
    """
    Calculates the range for a given list of numbers. Max number in range - Min number in range
        
    Args:
        numbers: A list of numbers for which the range is calculated
        
    Returns:
        The range for the list of given numbers.
    """
    sorted_numbers = sorted(numbers)
    max_num = sorted_numbers[0]
    min_num = sorted_numbers[0]

    return max_num - min_num

def calculate_variance(numbers):
    """
    Calculates the variance for a given list of numbers. 
            
    Args:
        numbers: A list of numbers for which the variance is calculated
            
    Returns:
        The variance for the list of given numbers.
    """
    mean = calulate_mean(numbers)
    squared_differences = []

    for n in numbers:
        difference = n - mean
        squared_differences.append(difference ** 2)

    return sum(squared_differences) / len(numbers)

def calculate_std(numbers):
    """
    Calculates the standard deviation for a given list of numbers. 
            
    Args:
        numbers: A list of numbers for which the standard deviation is calculated
            
    Returns:
        The standard deviation for the list of given numbers.
    """
    variance = calculate_variance(numbers)
    return variance ** 0.5

# 20. Write a function called greet which takes a default argument, name. If no argument is supplied it should print "Hello, Guest!", otherwise it should greet the person by name.
def greet(name="Guest"):
    """
    Returns a greeting message for the given name. 
                
    Args:
        name (str): The name of the person to greet. Defaults to "Guest".
                
    Returns:
        str: A greeting message.
    """
    if not name:
        return "Hello, Guest!"
    else:
        return f"Hello, {name}!"

# 21. Create a function called show_args to take an arbitrary number of named arguments and print their names and values.
def show_args(**info):
    """
    Prints the names and values of arbitrary keyword arguments. 
                    
    Args:
        **info (dict): An arbitrary number of named arguments.
                    
    Returns:
        None
    """
    for key, value in info.items():
        print(f"{key}: {value}")

# 22 . Write a function called is_prime, which checks if a number is prime.
def is_prime(n):
    """
    Checks whether a given integer is a prime number. 
                        
    Args:
        n (int): The integer to check for primality.
                        
    Returns:
        bool: True if the number is prime, otherwise False.
    """
    # Numbers less than or equal to 1 are not prime
    if n <= 1:
        return False
    # 2 is the only even prime number
    if n == 2:
        return True
    # Exclude all other even numbers
    if n % 2 == 0:
        return False
    # Check odd factors up to the square root of n
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False

    return True

# 23. Write a functions which checks if all items are unique in the list.
def all_unique(numbers):
    """
    Checks whether all elements in a list are unique. 
                        
    Args:
        numbers (list): A list of elements.
                        
    Returns:
        bool: True if all elements are unique, otherwise False.
    """
    for n in numbers:
        if numbers.count(n) > 1:
            return False

    return True

    
# 24. Write a function which checks if all the items of the list are of the same data type.
def same_data_type(items):
    """
    Checks whether all elements in a list have the same data type.

    Args:
        items (list): A list of elements.

    Returns:
        bool: True if all elements have the same data type,
              otherwise False.
    """
    if not items:
        return True

    first_type = type(items[0])

    for item in items:
        if type(item) != first_type:
            return False

    return True

# 25. Write a function which check if provided variable is a valid python variable
def is_valid_variable(variable):
    """
    Checks whether a string is a valid Python variable name.

    Args:
        variable (str): The variable name to validate.

    Returns:
        bool: True if valid, otherwise False.
    """
    return variable.isidentifier() and not variable.iskeyword()