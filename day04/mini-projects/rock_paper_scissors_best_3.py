print("=" * 50)
print("Rock, Paper, Scissors (Best of 3)")
print("=" * 50)

import random

CHOICES = ("rock", "paper", "scissors")
# what beats what: key beats value
BEATS = {"rock": "scissors", "paper": "rock", "scissors": "paper"}

player_wins = 0
computer_wins = 0

while player_wins < 2 and computer_wins < 2:
    player = input("\nRock, paper, or scissors? ").lower().strip()
    if player not in CHOICES:
        print("Invalid choice")
        continue

    computer = random.choice(CHOICES)
    print(f"Computer chose: {computer}")

    if player == computer:
        print("It's a tie!")
    elif BEATS[player] == computer:
        player_wins += 1
        print("You win this round!")
    else:
        computer_wins += 1
        print("Computer wins this round!")

    print(f"Score — You: {player_wins}  Computer: {computer_wins}")

if player_wins > computer_wins:
    print("\nYou win the match!")
else:
    print("\nComputer wins the match!")