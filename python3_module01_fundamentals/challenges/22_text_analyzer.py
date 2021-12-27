# Create a program that reads a person's full name and displays: 
# The name in all capital letters
# The name with all lowercase
# How many in total (not including spaces)
# How many letters does the first name have.

full_name = str(input('Enter a full name: ')).strip()

name_without_spaces = ''.join(full_name.split())
first_name = full_name.split()[0]

# space_counter = full_name.count(' ')

print('The fullname in uppercase is: {}'.format(full_name.upper()))
print('The fullname in lowercase is: {}'.format(full_name.lower()))
print('The name consists of {} letters'.format(len(name_without_spaces)))
print('The first name is {} and consists of {} letters'.format(first_name, len(first_name)))
print('The first name is {} and consists of {} letters'.format(first_name, full_name.find(' ')))