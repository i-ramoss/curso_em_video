# Make a program that reads a person's gender, but only accepts "M" or "F" values.
# If it is wrong, ask for the typing again until you have a correct value.

gender = str(input("Enter here your gender (F/M): ")).strip().upper()

while gender not in "MF":
    gender = str(input("Invalid data, enter here your gender (F/M): ")).strip().upper()

if gender == "F":
    print("Your gender is female.")

elif gender == "M":
    print("Your gender is male.")
