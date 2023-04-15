# Make an algorithm that reads an employee's salary and shows their new salary, with 15% of the increase

increase = 0.15

salary = float(input("Enter you current salary: R$"))

print(
    "With 15% of the increase, your new salary will be: R${:.2f}".format(
        salary + (salary * increase)
    )
)
