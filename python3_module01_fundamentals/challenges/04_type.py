# Make a program that reads something from the keyboard and displays its primitive type and all possible information about it on the screen

value = input('Enter a value: ')

print('The primitive type of the entered value is: {}.'.format(type(value)))
print('Is the value entered numeric?', value.isnumeric())
print('Is the value entered alpha numeric?', value.isalnum())
print('Is the value entered in uppercase?', value.isupper())
print('Is the value entered in lowercase?', value.islower())
print('Is the value entered title?', value.istitle())
print('Is the value entered space?', value.isspace())
print('Is the value entered alpha?', value.isalpha())