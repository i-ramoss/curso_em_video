# Write a program that uses any integer and ask the user to choose the base of conversion:
# 1 - to binary
# 2 - to octal
# 3 - to hexadecimal

integer = int(input("Enter a integer to be converter: "))

code = int(
    input(
        """Which number base do you want to convert to?\n
- Enter 1 for binary
- Enter 2 for octal
- Enter 3 for hexadecimal\n
Enter here: """
    )
)

print("Your option was: {}".format(code))

if code == 1:
    print("{} converted to BINARY equals: {:b}".format(integer, integer))
elif code == 2:
    print("{} converted to OCTAL equals: {:o}".format(integer, integer))
elif code == 3:
    print("{} converted to HEXADECIMAL equals: {:x}".format(integer, integer))
else:
    print("Invalid code, please enter a valid numeric base!")
