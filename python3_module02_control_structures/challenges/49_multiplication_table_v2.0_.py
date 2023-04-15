# Redo a challenge09, showing the multiplication table of a number that the user
# choose, only now using for loop

# Make a program that reads any integer and displayss your table

number = int(input("Enter a number to display its multiplication table: "))

for index in range(0, 11):
    print("{} X {:2} == {}".format(number, index, number * index))
