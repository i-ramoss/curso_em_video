# Write a program that reads the speed of a car.
# If goes over 80km/h, show a message saying he's been fined.
# The fine will cost R$7,00 for each km over the limit

car_speed = float(input("Enter your car's speed: "))

fine = (car_speed - 80) * 7

if car_speed > 80:
    print("You were fined!")
    print("You'll have to pay an amount of R${:.2f}".format(fine))
else:
    print("Everything is alright!")
