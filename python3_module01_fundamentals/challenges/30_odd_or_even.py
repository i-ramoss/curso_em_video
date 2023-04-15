# Create a program that reads an integer and shows on the screen whether it is odd or even.

number = int(input("Enter a number: "))

if number % 2 == 0:
    print("{} is an even number.".format(number))
else:
    print("{} is an odd number.".format(number))
