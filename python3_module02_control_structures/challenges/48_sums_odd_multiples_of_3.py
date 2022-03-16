# Write a program that calculates the sum of all of odd numbers that are multiples
# of three and that lie in the range 1 to 500.

sum = 0

for number in range(1, 501, 2):
    if number % 2 != 0 and number % 3 == 0:
        sum += number

print(
    "The sum of all odd numbers that are multiples of three in the range 1 to 500 is, "
    + str(sum)
)
