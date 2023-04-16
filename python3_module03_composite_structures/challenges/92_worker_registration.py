# Create a program that reads name, year of birth and work card and registers them
# (with age) in a dictionary. If by chance the CTPS (work card) is different from 0,
# the dictionary will also receive the year of hiring and the salary.
# Calculate and add, in addition to age, how many years the person will retire
# (35 years of contribution).

from datetime import date

worker = {}

worker["name"] = str(input("Name: "))

year_of_birth = int(input("Year of birth: "))
worker["age"] = date.today().year - year_of_birth

worker["work_card"] = int(input("Work card: (0 if not) "))

if worker["work_card"] != 0:
    worker["year_of_hire"] = int(input("Year of hire: "))
    worker["salary"] = float(input("Your current salary: R$ "))

    years_of_contributing = date.today().year - worker["year_of_hire"]

    if years_of_contributing < 35:
        worker["age_at_retirement"] = worker["age"] + (35 - years_of_contributing)
    else:
        worker["age_at_retirement"] = worker["age"]

for key, value in worker.items():
    print(f"- {key} has value: {value}")


# another way to get age_at_retirement

# worker["age_at_retirement"] = worker["age"] + (
#     (worker["year_of_hire"] + 35) - date.today().year
# )
