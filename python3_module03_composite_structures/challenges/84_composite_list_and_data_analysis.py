# Make a program that reads the name and weight of several people,
# keeping everything in a list. At the end, show:
# a) How many people were registered.
# b) A list of the heaviest people.
# c) A list of the lightest people.

people = []

print("To generate the list, add at least 2 people")

while True:
    person_name = str(input("\nName: "))
    person_weight = int(input("Weight: "))

    people.append([person_name, person_weight])

    add_more = str(input("\nDo you want add more people: [Y/N]:"))

    if add_more not in "yY":
        break

if len(people) < 2:
    print("Insufficient number of people")
    exit()

heaviest_people = [people[0].copy()]
lightest_people = [people[0].copy()]

heaviest = lightest = people[0][1]

for index, person in enumerate(people[1:], start=1):
    current_person_weight = person[1]

    # check the heaviest person
    if current_person_weight > heaviest:
        heaviest_people.clear()
        heaviest_people.append(person)
        heaviest = current_person_weight

    elif current_person_weight == heaviest:
        heaviest_people.append(person)

    # check the lightest person
    elif current_person_weight < lightest:
        lightest_people.clear()
        lightest_people.append(person)
        lightest = current_person_weight

    elif current_person_weight == lightest:
        lightest_people.append(person)

print(f"\nIn all you registered {len(people)} people.")
print(f"The highest weight was {heaviest}kg. Weight of", end=" ")

for person in heaviest_people:
    print(f"[{person[0]}]", end=" ")

print(f"\nThe lowest weight was {lightest}kg. Weight of", end=" ")

for person in lightest_people:
    print(f"[{person[0]}]", end=" ")

print()


################################################################################

# Other resolution (more simply)

# temporary_list = []
# people = []
# heaviest = lightest = 0

# print("To generate the list, add at least 2 people")

# while True:
#     temporary_list.append(str(input("Name: ")))
#     temporary_list.append(str(input("Weight: ")))

#     if len(people) == 0:
#         heaviest = lightest = temporary_list[1]

#     else:
#         if temporary_list[1] > heaviest:
#             heaviest = temporary_list[1]
#         if temporary_list[1] < lightest:
#             lightest = temporary_list[1]

#     people.append(temporary_list.copy())

#     temporary_list.clear()

#     add_more = str(input("\nDo you want add more people: [Y/N]:"))

#     if add_more not in "yY":
#         break

# print(f"\nIn all you registered {len(people)} people.")
# print(f"The highest weight was {heaviest}kg. Weight of", end=" ")

# for person in people:
#     if person[1] == heaviest:
#         print(f"[{person[0]}]", end=" ")

# print(f"\nThe lowest weight was {lightest}kg. Weight of", end=" ")

# for person in people:
#     if person[1] == lightest:
#         print(f"[{person[0]}]", end=" ")

# print()
