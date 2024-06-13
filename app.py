# Importing the necessary modules

import random
import time

# Define the game options
options = ["rock", "paper", "scissors"]

# Get user input
user_choice = input("Enter your choice (rock, paper, scissors): ").lower()

# Check if the user's choice is valid
while user_choice not in options:
    user_choice = input("Invalid choice. Enter your choice (rock, paper, scissors): ").lower()


# Generate computer's choice
computer_choice = random.choice(options)

# Print computer's choice
print("Computer chose:", computer_choice)

# Delay for suspense
time.sleep(1)

player_score = 0
computer_score = 0

 # Determine the winner
if user_choice == computer_choice:
    print("It's a tie!")
elif (user_choice == "rock" and computer_choice == "scissors") or (user_choice == "paper" and computer_choice == "rock") or (user_choice == "scissors" and computer_choice == "paper"):
    print("You win!")
    player_score += 1  
else:
    print("Computer wins!")
    computer_score += 1

# Ask e user if they want to play again

while True:
    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() == "yes":
        # Get user input
        user_choice = input("Enter your choice (rock, paper, scissors): ")
        # Generate computer's choice
        computer_choice = random.choice(options)
        # Print computer's choice
        print("Computer chose:", computer_choice)
        # Delay for suspense
        time.sleep(1)
        # Determine the winner
        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == "rock" and computer_choice == "scissors") or (user_choice == "paper" and computer_choice == "rock") or (user_choice == "scissors" and computer_choice == "paper"):
            print("You win!")
            player_score += 1  
        else:
            print("Computer wins!")
            computer_score += 1
    else:
        print("Thank you for playing!")
        break
print("Player score:", player_score)
print("Computer score:", computer_score)

# Calculate and print the final winner
if player_score > computer_score:
    print("Congratulations! You are the overall winner!")
elif player_score < computer_score:
    print("Better luck next time! The computer is the overall winner!")
else:
    print("It's a tie! No overall winner.")