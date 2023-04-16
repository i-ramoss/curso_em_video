# Improved Challenge 93 to work with multiplayer, including the detail view of
# each player's achievement system.

players = []
player = {}
goals = []
total_goals = 0

while True:
    name = str(input("Name: "))
    number_of_games = int(input("Number of games: "))

    for index in range(number_of_games):
        goal = int(input(f"How many goals in match {index + 1}? "))
        total_goals += goal

        goals.append(goal)

    player["name"] = name
    player["goals"] = goals.copy()
    player["total"] = total_goals

    players.append(player.copy())

    player.clear()
    goals.clear()
    total_goals = 0

    add_more_players = str(input("\nDo you want add more players: [y/n] ")).lower()

    print()

    if add_more_players != "y":
        break

# print(players)

for index, player in enumerate(players):
    print(
        f'Nº {index}    Name: {player["name"]}    Goals: {player["goals"]}    Total of goals: {player["total"]}'
    )


message = (
    "\nDo you want to see the information of a specific player? (Enter -1 to exit.) "
)
specific_player_code = int(input(message))

while specific_player_code != -1:
    specific_player = players[specific_player_code]

    print(f'\nPlayer {specific_player["name"]} posing: ')

    for index in range(len(specific_player["goals"])):
        print(f'=> On match {index + 1}, scored {specific_player["goals"][index]}.')

    print(f'Scored a total of {specific_player["total"]} goals.')

    specific_player_code = int(input(message))
