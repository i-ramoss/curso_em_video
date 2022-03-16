# Develop a programa that reads the first term and reason of an AP.
# At the end, show the first 10 terms of this progression.

first_term = int(input("Enter the first term to AP: "))
reason = int(input("Enter the reason of AP: "))

tenth_term = first_term + (10 - 1) * reason

for index in range(first_term, tenth_term + reason, reason):
    print(index, end=" -> ")

    first_term += reason

print("The arithmetic progression finish")