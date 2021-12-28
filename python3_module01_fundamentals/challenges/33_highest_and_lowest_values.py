# Make a program that reads tree numbers and shows which is the largest and which is the smallest

number01 = float(input('Enter the first number: '))
number02 = float(input('Enter the second number: '))
number03 = float(input('Enter the third number: '))

if (number01 < number02) & (number01 < number03): 
  smallest = number01
  
  if (number02 < number03): highest = number03
  else: highest = number02

elif (number02 < number01) & (number02 < number03):
  smallest = number02
  
  if (number01 < number03): highest = number03
  else: highest = number01
  
else:
  smallest = number03
  
  if (number01 < number02): highest = number02
  else: highest = number01
  
print('The smallest number is: {:.1f} and the highest is: {:.1f}.'.format(smallest, highest))