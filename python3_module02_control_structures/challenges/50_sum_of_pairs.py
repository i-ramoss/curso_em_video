# Develop a program that reads the integers and displays the sum of only those
# that are even.
# If the value entered is odd, disregard it.

counter = 0

for index in range(0, 6):
    number = int(input("Enter an integer: "))

    if number % 2 == 0:
        counter += number

print("The sum of all even numbers added is:", counter)
