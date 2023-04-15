# Write a program that reads two integers and compares them, displaying a message
# on the screen:

# The first value is higher;
# The second value is higher;
# There isn't higher value, the numbers are the same;

value_01 = int(input("Enter the first value: "))
value_02 = int(input("Enter the second value: "))

if value_01 > value_02:
    print("The first value, {}, is higher!\n".format(value_01))

elif value_01 < value_02:
    print("The second value, {}, is higher!\n".format(value_02))

else:
    print("There isn't higher value, the numbers are the same!")
