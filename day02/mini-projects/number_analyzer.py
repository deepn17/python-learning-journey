# Number Analyzer

user_input = input("Enter an integer: ").strip()

if not user_input:
    print("You didn't enter anything. Using default: 42")
    num = 42
elif user_input.lstrip("-").isdigit():
    num = int(user_input)
else:
    print("That's not a valid integer. Using default: 42")

if num > 0:
    sign = "positive"
elif num < 0:
    sign = "negative"
else:
    sign = "zero"


if num == 0:
    parity = "neither even or odd"
elif num % 2 == 0:
    parity = "even"
else:
    parity = "odd"


if num == 0:
    magnitude = ""
elif 0 < abs(num) <= 10:
    magnitude = "small"
elif 10 < abs(num) <= 100:
    magnitude = "medium"
elif 100 < abs(num) <= 1000:
    magnitude = "large"
else:
    magnitude = "huge"

facts = []
if num != 0 and num % 3 == 0:
    facts.append("divisible by 3")
if num != 0 and num % 5 == 0:
    facts.append("divisible by 5")
if num != 0 and num % 7 == 0:
    facts.append("divisible by 7")
    

print(f"\n📊 ANALYSIS: {num} is a {magnitude} {sign} number and is {parity}.")
if facts:
    print(f"   It is also {' and '.join(facts)}.")