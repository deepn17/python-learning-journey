"""
1. Declare four variables: your_name (str), your_age (int), your_height_cm (float), and is_beginner (bool).
Print each one along with its type().
"""

full_name = "First One"
age = 34
height_cm = 175.2
is_beginner = True

print(full_name, type(full_name))
print(age, type(age))
print(height_cm, type(height_cm))
print(is_beginner, type(is_beginner))

"""
2. Take the string "99", convert it to an int, add 1, and print the result and its type.
"""
num_str = "99"
num_int = int(num_str)
new_num = num_int + 1

print(new_num, type(new_num))

"""
3 .Add an int (7) and a float (2.5) together. Print the result and add a # comment explaining why the result is a float.
"""
int_num = 7
float_num = 2.5

total_num = int_num + float_num
print(total_num)    # The result is a float because when an int and a float are used in an arithmetic operation,
                    # Python automatically converts the int to a float and returns a float result.


"""
4. Use multiple assignment on one line: a, b, c = 5, 15, 25. Print their sum.
"""
a, b, c = 5, 15, 25
sum_abc = (a + b + c)
print(sum_abc)

"""
5. Bug hunt: given age = "30", the line print(age + 5) throws a TypeError. Why? Fix it.
"""
age_q5 = "30"
# print(age_q5 + 5)     # TypeError: can only concatenate str (not "int") to str
print(int(age_q5) + 5)

"""
6. Ask the user for two numbers (remember to cast them with int() or float()!) and print their sum, difference, product, and quotient.
"""
num_1 = int(input("Enter the first number: "))
num_2 = int(input("Enter the second number: "))

sum_of = num_1 + num_2
diff_of = num_1 - num_2
prod_of = num_1 * num_2
div_of = num_1 / num_2

print("Sum of the numbers are: ", sum_of)
print("Difference of the numbers are: ", diff_of)
print("Product of the numbers are: ", prod_of)
print("Quotient of the numbers are: ", div_of)

"""
7. BMI Calculator: input weight in kg and height in meters. Compute bmi = weight / height ** 2. Print it formatted to 2 decimal places.
"""
weight_kg = float(input("Enter your weight in kg: "))
height_m = float(input("Enter your height in meters: "))

bmi = weight_kg / (height_m ** 2)

print(f"BMI: {bmi:.2f}")

"""
8. Input a birth year. Compute age = current_year - birth_year. Print the result of age >= 18 — just the boolean, 
no if statement yet (that's tomorrow).
"""

birth_year = int(input("Enter your birth year: "))
current_year = 2026

age = current_year - birth_year

print(age >= 18)

"""
9. Input a number and print number % 2 == 0. That boolean is your even/odd answer — True means even, False means odd.
"""
check_num = int(input("Enter a number of your choice: "))

print("Is the number even?", check_num % 2 == 0)

"""
10. Temperature converter: input Celsius, convert to Fahrenheit with F = C * 9/5 + 32, print formatted to 1 decimal place.
"""
temp_in_c = float(input("Enter the temperature in Celsius: "))
converted_temp = temp_in_c * 9 / 5 + 32

print(f"The Fahrenheit Temperature is: {converted_temp:.1f}")