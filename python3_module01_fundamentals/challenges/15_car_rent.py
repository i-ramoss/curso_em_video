# Write a program that asks how many miles a rental car has traveled and how many days it has been rented. Calculate the price to pay,knowing that the car costs R$60 per day and R%0.15 per km driven.

cost_per_day = 60
cost_per_km = 0.15

days_rented = int(input("How many days was the car rented? "))
km_traveled = float(input("How many kilometers did you travel? Enter here: "))

price = (days_rented * cost_per_day) + (km_traveled * cost_per_km)

print(
    "Knowing that the daily costs R${} and R${} for each kilometer travelled, the total amount of the rent is: R${:.2f}".format(
        cost_per_day, cost_per_km, price
    )
)
