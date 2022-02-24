# The National Swimming Confederation needs a program that reads an athlete's
# year of birth and shows his category, according to age:

# Up to 9 years: MIRIM
# Up to 14 years: CHILD
# Up to 19 years: JUNIOR
# Up to 20 years: SENIOR
# Over 20 years: MASTER

from datetime import date

athlete_birth_year = int(input('Enter here your birth year, athlete: '))

if (len(str(athlete_birth_year)) > 4): 
  print ('Invalid year!')
  exit()

current_year = date.today().year

athlete_age = current_year - athlete_birth_year

categories = ['MIRIM', 'CHILD', 'JUNIOR', 'SENIOR', 'MASTER']

if (athlete_age <= 9): print('Your category is: {}'.format(categories[0]))
elif (athlete_age <= 14): print('Your category is: {}'.format(categories[1]))
elif (athlete_age <= 19): print('Your category is: {}'.format(categories[2]))
elif (athlete_age <= 20): print('Your category is: {}'.format(categories[3]))
else: print('Your category is: {}'.format(categories[4]))


