# Make a program that reads the name and average of a student, also saving the
# situation in a dictionary.
# At the end, show the contents of the structure on the screen.

name = str(input("Name: "))
grade_average = float(input(f"{name}'s average: "))

student = {
    "name": name,
    "average": grade_average,
    "situation": "Approved" if grade_average >= 7 else "Reproved",
}

print(
    f'{student["name"]} had an average of {student["average"]:.1f}! {student["situation"]}!'
)
