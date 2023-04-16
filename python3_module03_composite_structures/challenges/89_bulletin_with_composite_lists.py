# Create a program that reads the name and two notes of several students and
# saves everything in a composite list.
# At the end, show a bulletin containing the average of each one and allow the
# user to show the grades of each student individually.

students = []
auxiliar_list = []

while True:
    auxiliar_list.append(str(input("Name: ")))
    auxiliar_list.append(float(input("Note 1: ")))
    auxiliar_list.append(float(input("Note 2: ")))

    students.append(auxiliar_list.copy())

    auxiliar_list.clear()

    add_more_students = str(input("\nDo you want to add more students? [y/n]"))

    print()

    if add_more_students not in "yY":
        break

for index, student in enumerate(students):
    print(
        f"Nº: {index}    Name: {student[0]}    Average: {(student[1] + student[2]) / 2:.1f}"
    )

message = "\nDo you want to see the grades of a specific student? (Enter -1 to exit.)"
specific_student = int(input(message))

while specific_student != -1:
    print(
        f"\nNotes of {students[specific_student][0]} are [{students[specific_student][1]}, {students[specific_student][2]}]."
    )

    specific_student = int(input(message))
