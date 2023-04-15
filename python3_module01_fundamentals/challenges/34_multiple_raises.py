# Write a program that asks for an employee's salary and calculates the amount of his raise.
# For salaries above R$1250,00, calculate a 10% increase.
# For those who are inferior or equal, the increase is 15%.

salary = float(input("Enter your current salary: R$"))

if salary > 1250:
    new_salary = (salary * 0.1) + salary

else:
    new_salary = (salary * 0.15) + salary

print("You received a raise and your new salary is R${:.2f}".format(new_salary))
