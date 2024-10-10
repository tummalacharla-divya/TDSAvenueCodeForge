""" Rock, paper, scissors game
Create a program that allows the user to play
the classic game of rock, paper, scissors 
against the computer."""
import random

def get_computer_choice():
    # Computer randomly selects rock, paper, or scissors
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def get_user_choice():
    # Get user input and ensure it's valid
    while True:
        choice = input("Enter your choice (rock, paper, or scissors): ").lower()
        if choice in ['rock', 'paper', 'scissors']:
            return choice
        else:
            print("Invalid choice, please try again.")

def determine_winner(user_choice, computer_choice):
    # Determine the winner based on the rules of the game
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    # Get choices
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    
    # Display choices
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    
    # Determine and display the winner
    result = determine_winner(user_choice, computer_choice)
    print(result)

if __name__ == "__main__":
    play_game()
