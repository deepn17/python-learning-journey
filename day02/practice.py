# ============================================================
# PRACTICE 1: Temperature Classifier
# ============================================================
# Classify a temperature (in °C) into one of:
#   Below 0:    "Freezing"
#   0 to 15:    "Cold"
#   16 to 25:   "Mild"
#   26 to 35:   "Warm"
#   Above 35:   "Hot"

temperature = float(input("Enter the temperature: "))

if temperature < 0:
    print("Freezing")
elif temperature < 16:
    print("Cold")
elif temperature < 26:
    print("Mild")
elif temperature < 36:
    print("Warm")
else:
    print("Hot")

# the above range has been selected based on temperature being float, if int, then the range would change, like 0 <= temperature <= 15, <=16 temperature <= 25 etc etc.

# ============================================================
# PRACTICE 2: Largest of Three
# ============================================================
# Take three numbers as input and print the largest.
# Do NOT use the max() function — use if/elif/else.

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

if num1 >= num2 and num1 >= num3:
    print(f"{'num1'} is the largest of 3.")
elif num2 >= num1 and num2 >= num3:
    print(f"{'num2'} is the largest of 3.")
else:
    print(f"{'num3'} is the largest of 3.")

# the reason for >= is that even if num1 = 10, num2 = 10, then we will take the first occurence of that number as the largest of the 3.


# ============================================================
# PRACTICE 3: Vowel or Consonant Counter
# ============================================================
# Take a single character and print whether it's a vowel,
# consonant, digit, or special character.

vowel = ('a', 'e', 'i', 'o', 'u')
special_char = ('!', '@', '#', '$', '%', '^', '&', '*',
    '(', ')', '-', '_', '+', '=', '[', ']',
    '{', '}', '\\', '|', ';', "'", ':', '"',
    ',', '<', '>', '/', '?')


single_char = input("Enter a single character: ").lower()

if len(single_char) != 1:
    print("Please enter exactly one character.")
elif single_char.isdigit():
    print(f"Entered Single Character is a digit")
elif single_char in special_char:
    print(f"Entered Single Character is a special character")
elif single_char in vowel:
    print(f"{single_char} is a vowel.")
else:
    print(f"{single_char} is a vowel.")

# ============================================================
# PRACTICE 4: Shipping Cost Calculator
# ============================================================
# Calculate shipping cost based on order amount:
#   Under ₹500:    ₹50 shipping
#   ₹500 - ₹999:   ₹30 shipping
#   ₹1000 - ₹1999: FREE shipping
#   ₹2000+:        FREE shipping + "Express" upgrade

order_amount = float(input("Enter the Order Amount: "))

if order_amount <= 0:
    print('Order Amount cannot be negative or zero.')
elif order_amount < 500:
    print("Shipping Cost: ₹50")
elif order_amount < 1000:
    print("Shipping Cost: ₹30")
elif order_amount < 2000:
    print("Free Shipping")
else:
    print('Free Shipping + "Express" upgrade')


# ============================================================
# PRACTICE 5: Triangle Type
# ============================================================
# Take three side lengths and determine the triangle type:
#   Equilateral:  all three sides equal
#   Isosceles:    exactly two sides equal
#   Scalene:      no sides equal
#   Not a triangle: fails the triangle inequality
#     (each side must be less than the sum of the other two)


# ============================================================
# PRACTICE 6: Time of Day Greeting
# ============================================================
# Take the hour (0-23) and print an appropriate greeting:
#   5-11:    "Good Morning!"
#   12-16:   "Good Afternoon!"
#   17-20:   "Good Evening!"
#   21-4:    "Good Night!"
# Handle invalid hours.