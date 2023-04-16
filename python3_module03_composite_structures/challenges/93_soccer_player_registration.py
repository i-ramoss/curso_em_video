# Create a program that manages the performance of a soccer player.
# The program will read the player's name and how many games he played.
# Then you will read the number of goals scored in each match.
# In the end, all this will be stored in a dictionary.
# Including total goals scored during the league.

name = str(input("Name: "))
number_of_games = int(input("Number of games: "))

player = {}
goals = []
total_goals = 0

for index in range(number_of_games):
    goal = int(input(f"How many goals in match {index + 1}? "))
    total_goals += goal

    goals.append(goal)

player["name"] = name
player["goals"] = goals.copy()
player["total"] = total_goals

print(f'The player {player["name"]} played {number_of_games} games.')

for index in range(number_of_games):
    print(f'=> On match {index + 1}, scored {player["goals"][index]}.')

print(f'Scored a total of {player["total"]} goals')
