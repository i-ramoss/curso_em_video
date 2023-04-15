# Create a program that will read several numbers and put them in a list.
# After that, create two extra lists that will contain only the even and odd values entered, respectively.
# At the end, show the contents of the three generated lists.

numbers = [
    int(number)
    for number in input(
        "Enter as many numbers as you like, separated by spaces: "
    ).split()
]

even_numbers = []
odd_numbers = []

for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)
    else:
        odd_numbers.append(number)

print("\nNumbers:", numbers)
print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)
