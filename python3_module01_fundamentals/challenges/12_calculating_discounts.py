# Make an algorith that reads theprice of a product and shows its new price, with 5% off

discount = 0.05

price = float(input("Enter the product price: "))

print(
    "Appying the five percent of discount in this product price the final price is: R${:.2f}".format(
        price - (price * discount)
    )
)
