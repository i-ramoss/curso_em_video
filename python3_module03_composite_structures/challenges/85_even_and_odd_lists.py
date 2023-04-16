# Create a program where the user can type 7 numerical values and register them
# in a single list that keeps even and odd values separate.
# At the end, show the even and odd values in ascending order.

numbers = [[], []]

for index in range(7):
    number = int(input(f"Enter the {index + 1}º number: "))

    if number % 2 == 0:
        numbers[0].append(number)
    else:
        numbers[1].append(number)


print(f"\nEven numbers: {sorted(numbers[0])}")
print(f"Odd numbers: {sorted(numbers[1])}")
