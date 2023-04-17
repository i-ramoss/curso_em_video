# The filter consists of replacing the value of a pixel by the median value
# of a neighboring pixels (including the pixel itself).
# The median filter can be used to remove noise or smooth images.

example_matriz = [[5, 3, 4], [6, 0, 2], [1, 9, 8]]
value_list = []

print("Matrix before median filter:")
for line in range(3):
    print(example_matriz[line])

for line in range(3):
    for column in range(3):
        value_list.append(example_matriz[line][column])

value_list.sort()

example_matriz[1][1] = value_list[4]

print()
print("Matrix after median filter:")
for line in range(3):
    print(example_matriz[line])
