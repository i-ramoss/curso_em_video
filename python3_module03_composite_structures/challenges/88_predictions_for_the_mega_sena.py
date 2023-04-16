# Make a program that helps a MEGA SENA player to create guesses.
# The program will ask how many games will be generated and will raffle 6
# numbers between 1 and 60 for each game (without repetitions), registering
# everything in a composite list.

from random import randint
from time import sleep

number_of_games = int(input("Enter the amount of games you want: "))

games = []

counter = 0

for line in range(number_of_games):
    game_line = []

    while counter < 6:
        random_number = randint(1, 61)

        if random_number not in game_line:
            game_line.append(random_number)
            counter += 1

    games.append(game_line)
    counter = 0

for index, game in enumerate(games):
    print(f"Game {index + 1}: {sorted(game)}")
    sleep(1)
