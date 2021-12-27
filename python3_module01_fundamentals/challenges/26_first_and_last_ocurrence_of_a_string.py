# Make a program that reads a sentence from the keyboard and displays:
# How many times does the letter "A" appear
# In what position it appears the first time
# In what position it appears the last time

phrase = str(input('Enter a phrase: ')).strip().upper()

print('The letter A appears in the sentence {} times'.format(phrase.count('A')))
print('The first time the letter A appears is at position {}.'.format(phrase.find('A') + 1))
print('The last time the letter A appears is at position {}.'.format(phrase.rfind('A') + 1))