import random

player_score = 0
computer_score = 0
print("Welcome to Rock, Paper, Scissors!")
choices = ['rock', 'paper', 'scissors']

while True:
    player = input("Make your choice (rock, paper, or scissors): ").strip().lower()
    if player not in choices:
        print("Invalid Choice.")
        continue
    computer = random.choice(choices)
    print(f"You chose: {player}  |  Computer chose: {computer}")
    if player == computer:
        print("It's a tie!")
    elif (player == 'rock' and computer == 'scissors') or (player == 'scissors' and computer == 'paper') or (player == 'paper' and computer == 'rock'):
        print("You win this round!")
        player_score += 1
    else:
        print("Computer wins this round.")
        computer_score += 1
    print(f"Score: You {player_score} | Computer {computer_score}")
    again = input("Play again? (y/n): ").strip().lower()
    if again != 'y':
        print(f"Final Score: You {player_score} | Computer {computer_score}")
        break
