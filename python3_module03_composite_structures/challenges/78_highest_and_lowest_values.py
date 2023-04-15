# Make a program that reads 5 numeric values and stores them in a list.
# At the end, show which was the largest and smallest value typed and their respective positions in the list.

numbers = input("Enter 5 integer numbers: ").split()

highest_number = max(numbers)
smallest_number = min(numbers)

highest_number_position = []
smallest_number_position = []

for index, number in enumerate(numbers):
    if number == highest_number:
        highest_number_position.append(index)
    elif number == smallest_number:
        smallest_number_position.append(index)

print(
    f"The highest number is {highest_number} and your position(s) are {highest_number_position}."
)
print(
    f"The smallest number is {smallest_number} and your position(s) are {smallest_number_position}."
)
