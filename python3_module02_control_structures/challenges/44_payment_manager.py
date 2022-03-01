# Create a program that calculates the amount be paid for a product, considering
# its normal price and payments terms:

# Cash/check: 10% discount
# Cash on card: 5% discount
# Up to 2x on the card: normal price
# 3x or more on the card: 20% interest

product_price = float(input("Enter here the product price: R$"))

print("What will be the payment method? \n")
print('- Enter "cash" for cash payment with a 20% discount')
print('- Enter "card" for cash payment on the card with a 10% discount')
print(
    "- Enter '2x' to spread the normal value of the product in 2 installments on the card."
)
print(
    "- Enter '3x' to spread the purchase in 3 installments with 20% interest on the card\n"
)
print(
    "- For any other entry, 20% interest will be added to the original value of the product\n"
)

payment_method = str(input("Enter here your payment method: ")).strip().lower()

payment_methods = ["cash", "card", "2x", "3x"]

if not payment_method in payment_methods or payment_method == "3x":
    print(
        "\nYou will have 20% interest. The final value will be R${:.2f}".format(
            product_price + (product_price * 0.2)
        )
    )

elif payment_method == "cash":
    print(
        "\nYou will get 20% off. The final value will be R${:.2f}".format(
            product_price - (product_price * 0.2)
        )
    )

elif payment_method == "card":
    print(
        "\nYou will get 10% off. The final value will be R${:.2f}".format(
            product_price - (product_price * 0.1)
        )
    )

elif payment_method == "2x":
    print("\nYou will divide the original value of the product int 2 installments.")
