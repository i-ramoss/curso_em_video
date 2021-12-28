# Develop a program that asks the distance of a trip in km.
# Calculate the price of the ticket, charging R$0,50 per km for trips of up to 200km and R$0,45 for longer trips

distance = float(input('Enter the distance to the destination in km: '))

ticket = distance * 0.5 if distance <= 200 else distance * 0.45

print('The price of the ticket is: R${:.2f}'.format(ticket))