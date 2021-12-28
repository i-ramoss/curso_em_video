note01 = float(input('Enter your first grade: '))
note02 = float(input('Enter your second grade: '))

average = (note01 + note02) / 2

print('You\'re approved! Congrats!') if average >= 5 else print('You\'re reproved! You need to study more.')