import random

# Define a list of possible choices
choices = ["rock", "paper", "scissors"]

# Ask the user to input their choice
user_choice = input("Choose rock, paper, or scissors: ").lower()

# Generate a random choice for the computer
computer_choice = random.choice(choices)

# Determine the winner
if user_choice == computer_choice:
    print("Tie!")
elif user_choice == "rock":
    if computer_choice == "paper":
        print("You lose! Paper covers rock.")
    else:
        print("You win! Rock smashes scissors.")
elif user_choice == "paper":
    if computer_choice == "scissors":
        print("You lose! Scissors cut paper.")
    else:
        print("You win! Paper covers rock.")
elif user_choice == "scissors":
    if computer_choice == "rock":
        print("You lose! Rock smashes scissors.")
    else:
        print("You win! Scissors cut paper.")
else:
    print("Invalid input. Please choose rock, paper, or scissors.")
