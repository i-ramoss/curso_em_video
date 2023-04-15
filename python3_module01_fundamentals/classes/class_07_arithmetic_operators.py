# name = input('What is your name? ')
# print('Nice to meet you {:=^20}!'.format(name))

number01 = 4
number02 = 3

print(
    "The sum between {} and {} is {}, \nthe product is {} and the division is {:.2f}.".format(
        number01,
        number02,
        number01 + number02,
        number01 * number02,
        number01 / number02,
    ),
    end=" ",
)
print(
    "The integer division is {} and the power is {}".format(
        number01 // number02, number01**number02
    )
)
