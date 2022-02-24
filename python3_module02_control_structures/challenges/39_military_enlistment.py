# Make a program that reads a young persons' year of birth and reports, according
# to their age:

# If he's still going to enlist in the military;
# If it's time to enlist;
# If it is past the time of enlistment;

# Your program should also show the time left or overdue;

from datetime import date

candidate_birth_year = int(input('Enter the year of your birth: '))

if (len(str(candidate_birth_year)) > 4): 
  print ('Invalid year!')
  exit()

current_year = date.today().year

difference_between_years = current_year - candidate_birth_year

if (difference_between_years == 0):
  print('You must fo to military enlistment this year! Don\'t forget!')

elif (difference_between_years < 18):
  print('You must enlist for military service in {} years.'
    .format(18 - difference_between_years))

elif (difference_between_years > 18):
  print('It has been {} years since your military enlistment.'
    .format(difference_between_years - 18))