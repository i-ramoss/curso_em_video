# Create a program where 4 players throw a dice and have random results.
# Store these results in a dictionary. In the end, put that dictionary in order,
# knowing that the winner got the highest number on the dice.

from random import randint

players = {}
highest = 0

for index in range(4):
    name = str(input("Name: ")).strip()

    dice_value = randint(1, 6)

    if dice_value > highest:
        highest = dice_value

    players[name] = dice_value

position = 1

for player in sorted(players, key=players.get, reverse=True):
    print(f"{position}º place: {player} with {players.get(player)}")
    position += 1

#################

# other resolutions

print()

ranking = {
    key: value
    for key, value in sorted(players.items(), key=lambda item: item[1], reverse=True)
}

print(f"Ranking with lambda function {ranking}")

from operator import itemgetter

ranking = sorted(players.items(), key=itemgetter(1), reverse=True)

print(f"Ranking with itemgetter operator method {ranking}")
