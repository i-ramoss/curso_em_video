# Create a program that makes the computer play Jokenpo with you

from time import sleep
from random import choice

print("I want to see if you can beat me at Jokenpo! Good luck\n")

print("Your options are: 'rock', 'paper' and 'scissors'.\n")

computer_options = ["rock", "paper", "scissors"]

username = str(input("What is your name? ")).strip()
user_choice = (
    str(input("Nice to meet you, {}. Now, make your choice: ".format(username)))
    .strip()
    .lower()
)

while not user_choice in computer_options:
    user_choice = str(input("\nInvalid choice. Try again: ")).strip().lower()

user_wins = 0
computer_wins = 0

while user_choice in computer_options:
    print("\nJokennnnnn", end="")
    sleep(1)
    print("pooooo!!!\n")

    print("{} VS COMPUTER".format(username))

    computer_choice = choice(computer_options)

    if user_choice == "rock":
        if computer_choice == "scissors":
            user_wins += 1
            print("🪨  X ✂ " + "." * 15 + "You win! Congrats\n")
        elif computer_choice == "paper":
            computer_wins += 1
            print("🪨  X 📰 " + "." * 15 + "You lose! HAHAHA!\n")
        else:
            print("🪨  X 🪨  " + "." * 15 + "A TIE!\n")

    elif user_choice == "paper":
        if computer_choice == "rock":
            user_wins += 1
            print("📰 X 🪨  " + "." * 15 + "You win! Congrats\n")
        elif computer_choice == "scissors":
            computer_wins += 1
            print("📰 X ✂ " + " . " * 15 + "You lose! HAHAHA!\n")
        else:
            print("📰 X 📰 " + "." * 15 + "A TIE!\n")

    elif user_choice == "scissors":
        if computer_choice == "paper":
            user_wins += 1
            print("✂ X 📰 " + "." * 25 + "You win! Congrats\n")
        elif computer_choice == "rock":
            computer_wins += 1
            print("✂ X 🪨  " + "." * 25 + "You lose! HAHAHA!\n")
        else:
            print("✂ X ✂ " + "." * 25 + "A TIE!\n")

    else:
        print("Error! Enter a valid choice!")

    print("Do you want to play again?\n")

    play_again = (
        str(input("Enter 'yes' to continue or 'no' to exit and show the final score: "))
        .strip()
        .lower()
    )

    print("\n\n" + "=" * 80 + "\n")

    if play_again == "yes":
        user_choice = str(input("\nMake your choice: ")).strip().lower()
    else:
        break

print("\nThat was AMAZING, and the FINAL SCORE was...\n")

if user_wins > computer_wins:
    print("{} VS {} for you!! You're a good player!\n".format(user_wins, computer_wins))

elif computer_wins > user_wins:
    print("{} VS {} for me!! I'm a invencible haha!\n".format(computer_wins, user_wins))

else:
    print("{} VS {}. We tie! What a contested game!\n".format(user_wins, computer_wins))
