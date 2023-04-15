# A teacher wants to draw one of his four students to erase the board. Make a programa that helps him by reading their name and writing the chosen name.

from random import choice

student01 = input("Enter a student name: ")
student02 = input("Enter a second student name: ")
student03 = input("Enter a third student name: ")
student04 = input("Enter a fourth student name: ")

students = [student01, student02, student03, student04]

print("The chosen student is {}!!".format(choice(students)))
