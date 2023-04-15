# The same teacher from the previous challenge wants to draw the order in which student's works is presented. Make a program that reads the names of the four students and shows the order drawn.

from random import sample

student01 = input("Enter a student name: ")
student02 = input("Enter a second student name: ")
student03 = input("Enter a third student name: ")
student04 = input("Enter a fourth student name: ")


students = [student01, student02, student03, student04]

print(
    "The order of presentation of students will be: {}".format(
        sample(students, k=len(students))
    )
)
