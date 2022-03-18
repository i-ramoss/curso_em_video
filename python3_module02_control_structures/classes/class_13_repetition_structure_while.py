value = 9

even = odd = 0

while value != 0:
    value = int(input("Enter a value: "))

    if value % 2 == 0:
        even += 1
    else:
        odd += 1

print("You enter {} even numbers and {} odd numbers".format(even, odd))
