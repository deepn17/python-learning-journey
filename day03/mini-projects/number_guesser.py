import random

print("=" * 60)
print("        Welcome to Number Guesser")
print("=" * 60)

# difficulty level
print("\n--- Choose Your Difficulty Level ---")
print("1. Easy   (1 - 10, unlimited guesses)")
print("2. Medium (1 - 50, 10 guesses)")
print("3. Hard   (1 - 100, 7 guesses)")

while True:
    level = input("Pick a level (1 - 3): ").strip()
    if level in ("1", "2", "3"):
        break
    print("Invalid choice. Please enter 1, 2, or 3.")

# set the range and guess limit based on difficulty level
if level == "1":
    max_num, max_guesses = 10, 999
elif level == "2":
    max_num, max_guesses = 50, 10
else:
    max_num, max_guesses = 100, 7

# set the secret number. random.randint(a, b) picks a random integer between a and b (inclusive).
secret = random.randint(1, max_num)

attempts = 0              # counts how many guesses the user made
guessed_correctly = False # "flag" that records whether they won

print(f"\nI'm thinking of a number between 1 and {max_num}.")
print(f"You have {max_guesses} guesses. Good luck!")

# The main game loop
while attempts < max_guesses:
    remaining = max_guesses - attempts
    guess_input = input(f"\nGuess #{attempts + 1} ({remaining} left): ").strip()

    # --- Input validation ---
    if not guess_input.lstrip("-").isdigit():
        print("That's not a valid number. Try again.")
        continue

    guess = int(guess_input)
    attempts += 1            # only count valid guesses

    # --- Check the guess ---
    if guess < 1 or guess > max_num:
        print(f"Out of range! Guess between 1 and {max_num}.")
    elif guess < secret:
        print(f"Too low!")
    elif guess > secret:
        print(f"Too high!")
    else:
        guessed_correctly = True
        break

# results and rating the play
if guessed_correctly:
    print(f"CORRECT! The number was {secret}.")
    print(f"You got it in {attempts} attempt(s).")

    # rate the play
    if attempts == 1:
        print(f"PERFECT! First try - are you a psychic?")
    elif attempts <= 3:
        print(f"Excellent guessing!")
    elif attempts <= 5:
        print(f"Not bad at all.")
    else:
        print("You got there eventually.")
else:
    print(f"Out of guesses! The number was {secret}.")
    print("Better luck next time.")

# additional feature
print("\n--- Number Line ---")
for i in range(1, max_num + 1):
    if i == secret:
        print("*", end=" ")
    else:
        print(".", end=" ")
print()

# play again
print("\n--- Play again ---")
while True:
    again = input("Play again? (yes/no): ").lower().strip()
    if again in ("yes", "y"):
        print("Restart the program to play again!")
        break
    elif again in ("no", "n"):
        print("Thanks for playing!")
        break
    else:
        print("Please answer yes or no.")

print("\n" + "=" * 60)
print("  Thanks for playing the Number Guesser!")
print("=" * 60)