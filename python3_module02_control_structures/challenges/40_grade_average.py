# Create a program that reads two students grades and calculates their average,
# showing a message at the end, according to the average achieved:

# Average below 5.0: FAIL;
# Average between 5.0 and 6.9: RECOVERY;
# Average 7.0 or higher: PASS;

note_01 = float(input('Enter here your first note: '))
note_02 = float(input('Enter here your second note: '))

if ((note_01 + note_02) > 20 or (note_01 + note_02) < 0):
  print('Invalid notes')
  exit()

average = (note_01 + note_02) / 2

if (average < 5.0): 
  print('Your average is {:.1f}, sorry, you FAIL.'.format(average))

elif (5.0 <= average <= 6.9):
  print('Your average is {:.1f}, sorry, you are on RECOVERY.'.format(average))

else:
  print('Congrats! Your average is {:.1f}, you are APPROVED!'.format(average))
