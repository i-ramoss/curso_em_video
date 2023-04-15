# Create a program that will read several numbers and put them in a list.
# After that show:
# a) How many numbers were entered
# b) The list of values, sorted in descending order.
# c) If the value 5 was typed and is or is not in the list.

# numbers = [int(number) for number in inpu().split()]
numbers = list(
    map(int, input("Enter as many numbers as you like, separated by spaces: ").split())
)

numbers.sort(reverse=True)
five_is_on_the_list = "is" if 5 in numbers else "is not"

print()
print(f"{len(numbers)} numbers have been added.")
print(f"List of added values in descending order: {numbers}")
print(f"Number 5 {five_is_on_the_list} on the list.")
