# Make a program that reads any year and shows if it is a leap year

from datetime import date

year = int(input('Enter a year. Put 0 do analyze the current year: '))

if year == 0: year = date.today().year

if (year % 4 == 0) & (year % 100 != 0) | (year % 400 == 0):
  print('The year of {} is a leap year.'.format(year))
elif (year % 4 != 0) & (year % 400 == 0):
  print('This is a leap year.')
else:
  print('The year of {} isn\'t a leap year.'.format(year))