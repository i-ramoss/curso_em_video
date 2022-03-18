# Develop a program that reads the name, age and gender of 4 people.
# At the end of the program show:

# - The average age of the group
# - What is the name of the oldest man
# - How many women are under 20 years old

group_average_age = 0
name_of_oldest_man = ""
women_under_twenty_years = 0

age_of_the_oldest_man = 0

for index in range(1, 5):
    print("----- {}º PERSON -----".format(index))

    person_name = str(input("Name: ")).strip()
    person_age = int(input("Age: "))
    person_gender = str(input("Gender [M/F]: ")).strip().upper()

    if person_gender != "M" and person_gender != "F":
        print("\nInvalid gender code.")
        exit()

    elif person_gender == "M":
        if person_age > age_of_the_oldest_man:
            age_of_the_oldest_man = person_age
            name_of_oldest_man = person_name

    else:
        if person_age > 20:
            women_under_twenty_years += 1

    group_average_age += person_age

    print("\n")

print("\nThe average age of the group is {:.1f}".format(group_average_age / 4))
print("The name of the the oldest man is:", name_of_oldest_man)
print(
    "There is {} woman under 20 years old.".format(women_under_twenty_years)
    if women_under_twenty_years == 1
    else "There are {} women under 20 years old.".format(women_under_twenty_years)
)
