# Create a program where the user can type five numerical values and register
# them in a list, already in the correct insertion position (without using sort()).
# At the end, show the sorted list on the screen.

numbers = []

for index in range(5):
    number = int(input(f"Enter the {index + 1}º digit: "))

    if index == 0 or number > numbers[-1]:
        numbers.append(number)

    else:
        for j_index, inside_list_number in enumerate(numbers):
            if number < inside_list_number:
                numbers.insert(j_index, number)
                break

print("\nOrdered list:", numbers)
