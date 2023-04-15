# Create an algorithm that reads a number and display it double, triple and square root

number = int(input("Enter a number: "))

print(
    "The double of {} is {}, the triple is {} and the square root is {:.2f}.".format(
        number, pow(number, 2), pow(number, 3), pow(number, 1 / 2)
    )
)
