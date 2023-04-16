# Create a program that creates a 3x3 dimension matrix and fills it with values read from the keyboard.
# At the end, show the matrix on the screen, with the correct formatting.

matriz = []

for line in range(3):
    matriz_line = []

    for column in range(3):
        matriz_line.append(int(input(f"Enter a number for {[line, column]}: ")))

    matriz.append(matriz_line)

for line in range(3):
    print(matriz[line])

################################################################################

# Other solution

# matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# for line in range(3):
#     for column in range(3):
#         matriz[line][column] = int(input(f"Enter a number for {[line, column]}: "))

# for line in range(3):
#     print(matriz[line])
