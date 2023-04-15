# snack = "burguer", "juice", "pizza", "pudding" - works without parentheses
snacks = ("burguer", "juice", "pizza", "pudding")

print("Snack:", snacks[0])
print("Snack:", snacks[-1])
print("Snack:", snacks[-3:])
print("Snack(s):", snacks[1:3])
print("Snack(s):", snacks[:3])
print("Snack(s):", snacks[::-1])

# tuples are immutable
# snacks[0] = "apple" - return error

print()

# Print snacks tuple sorted -> transform to list
print(sorted(snacks))

print()

# for without index
for snack in snacks:
    # f-strings notation
    print(f"I eat {snack} today")

print()

# for with index
for index, snack in enumerate(snacks):
    print(f"I eat {snack} today. And {snack} is in the position {index} on tuple.")

print()

# for with index (second way)
for index in range(0, len(snacks)):
    print(
        f"I eat {snacks[index]} today. And {snacks[index]} is in the position {index} on tuple."
    )

# delete a tuple entirely, only 1 or more items from the tupla cannot be deleted
del snacks
