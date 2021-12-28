name = str(input('Enter a name: ')).strip()

if name == 'Flora': print('This is a beautiful name!')

elif name == 'Cecilia' or name == 'Pietra' or name == 'Leandra':
  print('That is a amazing name!')

elif name in 'Ana Maria Cris Eduarda': print('This name are veryu common in Brazil! Wow!')

print('Nice to meet you, {}. Have a nice day!'.format(name))