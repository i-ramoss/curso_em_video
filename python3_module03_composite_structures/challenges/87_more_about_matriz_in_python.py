# Improve the previous challenge, showing at the end:
# a) The sum of all even values entered
# b) The sum of the values in the third column.
# c) The largest value in the second row.

matriz = []
sum_even_values = third_column_sum = highest_value_second_row = 0

for line in range(3):
    matriz_line = []

    for column in range(3):
        value = int(input(f"Enter a number for {[line, column]}: "))

        if value % 2 == 0:
            sum_even_values += value

        if column == 2:
            third_column_sum += value

        if line == 1 and value > highest_value_second_row:
            highest_value_second_row = value

        matriz_line.append(value)

    matriz.append(matriz_line)

for line in range(3):
    print(matriz[line])

print(f"\nThe sum of all even values is: {sum_even_values}")
print(f"The sum of the third column values is: {third_column_sum}")
print(f"The highest value of the second row is: {highest_value_second_row}")
