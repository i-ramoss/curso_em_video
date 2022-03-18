# Create a program that reads the birth year of seven people.
# At the end, show how many people have no yet reached the age of majority and
# how many are already older.
# the age of majority in this case is considered above or equal to 21 years.

from datetime import date

people_on_majority = 0

current_year = date.today().year

for index in range(0, 7):
    year = int(input("Please enter here your birth year: "))

    if current_year - year >= 21:
        people_on_majority += 1

print(
    "\nOf the 7 people, only {} have reached the age of majority!".format(
        people_on_majority
    )
)
