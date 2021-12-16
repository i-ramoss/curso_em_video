# Develop a program that reads a student's two grades, calculates and display their average

grade01 = int(input('Enter the first grade: '))
grade02 = int(input('Enter the second grade: '))

print("The student's final grade is {:.1f}!".format((grade01 + grade02) / 2))