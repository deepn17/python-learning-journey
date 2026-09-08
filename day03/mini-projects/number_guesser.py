print("=" * 60)
print("        Welcome to Number Guesser")
print("=" * 60)

# difficulty level
print("\n--- Choose Your Difficulty Level ---")
print("1. Easy   (1 - 10, unlimited guesses)")
print("2. Medium (1 - 50, 10 guesses)")
print("3. Hard   (1 - 100, 7 guesses)")

level = input("Pick a level (1 - 3): ").strip()
if level in ("1", "2", "3"):
    print("Proceed")
else:
    print("Invalid choice. Please enter 1, 2, or 3.")

# set the range and guess limit based on difficulty level
if level == "1":
    max_num, max_guesses = 10, 999
elif level == "2":
    max_num, max_guesses = 50, 10
else:
    max_num, max_guesses = 100, 7

print(f"Maximum Number: {max_num}, Maximum Guesses:  {max_guesses}")