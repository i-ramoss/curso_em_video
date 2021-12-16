# Create a program that reads how much money a person has in their wallet and shjows how many dollars they can buy

current_dollar_quote = 5.708

money = float(input('How many reais do you have to buy dollars? Enter here: '))

print('With your R${:.2f} you can buy ${:.2f}. Good luck'.format(money, money / current_dollar_quote))