print("=" * 50)
print("Word Guessing Game")
print("=" * 50)

secret = "python"
guessed = set()
lives = 6

while lives > 0:
    display = "".join(ch if ch in guessed else "-" for ch in secret)
    print(f"\nWord: {display}")
    print(f"Lives: {lives}  Guessed: {sorted(guessed)}")

    if display == secret:
        print("You win")
        break

    guess = input("Guess a letter: ").lower().strip()
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue

    if guess in guessed:
        print("You already guessed that letter.")
        continue

    guessed.add(guess)

    if guess not in secret:
        lives -= 1
        print(f"'{guess}' is not in the word")
else:
    print(f"\n Out of lives! The word was '{secret}'")
