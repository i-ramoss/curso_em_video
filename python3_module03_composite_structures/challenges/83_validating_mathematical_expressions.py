# Create a program where the user types any expression that uses parentheses.
# Your program should analyze if the passed expression has the open and closed parentheses in the correct order.

expression = input("Enter a expression: ")

expression_sliced = []

for char in expression:
    expression_sliced.append(char)

left_parentheses_counter = expression_sliced.count("(")
right_parentheses_counter = expression_sliced.count(")")

if left_parentheses_counter == right_parentheses_counter:
    print("The expression is correct.")
else:
    print(f"The expression isn't correct.")
