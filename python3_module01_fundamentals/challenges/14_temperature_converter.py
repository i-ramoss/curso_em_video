# Write a program thaat reads a value in Celsius degreens and converts it to Fahreinheight degrees.

celsius = float(input('Enter a value of a temperature in degrees Celsius: '))

print('The temperature of {}ºC corresponds to {:.1f}ºF.'.format(celsius, celsius * 1.8 + 32))