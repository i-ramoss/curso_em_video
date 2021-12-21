# Create a program that reads any real number on the keyboard and displays your integer part on the screen.

from math import trunc, floor

number = float(input('Enter a real number: '))

print('The integer part of the number {}, using truncate function, is {}.'.format(number, trunc(number)))
print('The integer part of the number {}, using floor function, is {}.'.format(number, floor(number)))
print('The integer part of the number {}, using int type, is {}.'.format(number, int(number)))