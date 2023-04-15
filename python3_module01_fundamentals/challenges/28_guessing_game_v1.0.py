# Write a program that makes the computer "think" of an integer between 0 and 5 and ask the user to try to figure out which number was chosen by the computer.
# The program should write on the screen if the user won or lost.

from random import randint
from time import sleep

choice = int(input("I'll think of a number between 0 and 5. Try to guess: "))

randomNumber = randint(0, 5)

print("Analyzing...")

sleep(2)

if choice == randomNumber:
    print("Congrats! You're right!")
else:
    print(
        "You missed. I thought of number {} and you type in {}. Try again!".format(
            randomNumber, choice
        )
    )
