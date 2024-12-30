import random

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)
    return roll

# Get the number of players
while True:
    players = input("How many players will be playing? Please enter a number between 2 and 4: ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("The number of players must be between 2 and 4. Please try again.")
    else:
        print("Invalid input. Please enter a number.")

# Game setup
max_score = 50
player_scores = [0 for _ in range(players)]

# Game loop
while max(player_scores) < max_score:
    for player_idx in range(players):
        print(f"\nIt's Player {player_idx + 1}'s turn!")
        print(f"Your total score so far is: {player_scores[player_idx]}\n")
        current_score = 0

        # Player's turn
        while True:
            should_roll = input("Would you like to roll the dice? Enter 'y' to roll, or any other key to hold your score: ")
            if should_roll.lower() != "y":
                break

            value = roll()
            if value == 1:
                print("Oh no! You rolled a 1. Your turn is over, and you earn no points this round!")
                current_score = 0
                break
            else:
                current_score += value
                print(f"Great! You rolled a {value}. Your score for this turn is now {current_score}.")

        player_scores[player_idx] += current_score
        print(f"Player {player_idx + 1}, your total score is now: {player_scores[player_idx]}")

# Determine the winner
max_score = max(player_scores)
winning_idx = player_scores.index(max_score)
print(f"\nCongratulations, Player {winning_idx + 1}! You are the winner with a total score of: {max_score}!")
