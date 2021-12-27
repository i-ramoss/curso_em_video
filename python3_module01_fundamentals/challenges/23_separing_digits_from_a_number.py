# Write a program that reads a number from 0 to 9999 and displays each of its separate digits on the screen.

number = int(input('Enter a number: '))

unit = number // 1 % 10
ten = number // 10 % 10
hundred = number // 100 % 10
thousands = number // 1000 % 10

print('Unit: {}\nTen: {}\nHundred: {}\nThousands: {}'.format(unit, ten, hundred, thousands))