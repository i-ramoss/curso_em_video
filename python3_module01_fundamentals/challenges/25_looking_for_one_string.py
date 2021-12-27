# Create a program that reads a person's name and tells them if they have 'SILVA' in their name

name = str(input('Enter your name: ')).strip()

print('Does your name have SILVA? {}'.format('SILVA' in name.upper()))