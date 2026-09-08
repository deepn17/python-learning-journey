print("=" * 60)
print("        Welcome to Number Guesser")
print("=" * 60)

# difficulty level
print("\n--- Choose Your Difficulty Level ---")
print("1. Easy   (1 - 10, unlimited guesses)")
print("2. Medium (1 - 50, 10 guesses")
print("3. Hard   (1 - 100, 7 guesses")

level = input("Pick a level (1 - 3): ").strip()
if level in ("1", "2", "3"):
    print("Proceed")
else:
    print("Invalid choice. Please enter 1, 2, or 3.")

# set the range and guess limit based on difficulty level
