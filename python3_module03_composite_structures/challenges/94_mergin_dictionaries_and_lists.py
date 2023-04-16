# Create a program that reads the name, sex and age of several people,
# keeping each person's data in a dictionary and all dictionaries in a list.
# At the end, show:
# a) How many people were registered.
# b) The average age of the group.
# c) A list of all women.
# d) A list of all people above average age.

data = []
person = {}
sum_of_ages = 0

while True:
    person["name"] = str(input("Name: "))
    person["sex"] = str(input("Sex [M/F]: ")).upper()
    person["age"] = int(input("Age: "))

    sum_of_ages += person["age"]

    data.append(person.copy())

    # person.clear()

    add_more_person = str(input("\nDo you want to add more people? [y/n] "))

    print()

    if add_more_person not in "yY":
        break

average_age = sum_of_ages / len(data)

print(f"a) Altogether we have {len(data)} people registered")
print(f"b) The average of age is {average_age:.1f}.")
print(f"c) The registered women were:", end=" ")

for person in data:
    if person["sex"] == "F":
        print(f'{person["name"]} ', end="")

print(f"\nd) List of people who are above average: ")

for person in data:
    if person["age"] > average_age:
        print(f'name = {person["name"]}; sex = {person["sex"]}; age = {person["age"]}; ')
