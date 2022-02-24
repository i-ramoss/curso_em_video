# Write a program to approve the bank loan for a home purchase. The program will ask the value of the house, the buyer's salary and in how many years he will pay.
# Calculate the amount of the monthly payment, knowing that it cannot exceed 30% of salary or the loan will be denied.

houseValue = float(input('Enter the value of the house: R$'))

buyerSalary = float(input('Enter your salary: R$'))

years = int(input('How many years do you intend to finance this house? Enter here: '))

monthlyPayment = houseValue / (years * 12)

print(
  '''The montly fee will be R${:.2f}. 
This amount needs to be less than 30% of your salary, which corresponds to R${:.2f}'''
  .format(monthlyPayment, buyerSalary * 0.3)
)

if monthlyPayment > (buyerSalary * 0.3): 
  print('You do not meet the requeriments to take out this loan, sorry!')
else:
  print('The loan can be made! We will shortly request the necessary documentation.')