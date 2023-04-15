# Make a program that reads the weight of fice people.
# At the end, show which was the highest and lowest weight read.

heaviest = 0
lightest = 0

for index in range(1, 6):
    weight = float(
        input("Enter here the weight of the {}º person (in kg): ".format(index))
    )

    if index == 1:
        heaviest = weight
        lightest = weight

    else:
        if weight > heaviest:
            heaviest = weight

        elif weight < lightest:
            lightest = weight

print("\nThe heaviest person weights {:.1f}kg.".format(heaviest))
print("The lightest person weights {:.1f}kg.".format(lightest))
