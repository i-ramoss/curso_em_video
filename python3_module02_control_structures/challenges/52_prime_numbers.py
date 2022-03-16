# Write a program and tell whether or not it is prime numbers

number = int(input("Enter the number here: "))

for index in range(2, number):
    if number % index == 0:
        print('This number is not prime.')
        exit()
    
print("This number is prime.")