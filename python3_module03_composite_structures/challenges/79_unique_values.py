# Create a program where the user can type several numeric values and register them in a list.
# If the number already exists there, it will not be added.
# At the end, all unique values entered will be displayed, in ascending order.

number = 0
numbers = []

while number != -1:
    number = int(
        input(
            "Enter a integer number to add to the list and enter a negative number to print and exit to the program: "
        )
    )

    if number not in numbers and number > 0:
        numbers.append(number)

print("\nThe list:", numbers)
