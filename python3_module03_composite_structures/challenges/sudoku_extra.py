# In Sudoku, each row and column needs to have numbers from 1 to 9, without repetitions.
# Each 3x3 quadrant must also contain numbers from 1 to 9, with no repetitions.
# Given a Sudoku game matrix, how to check if it was filled correctly?

matriz_sudoku = [
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9],
]

line_error = -1
column_error = -1
quadrant_error = -1

# check the lines
for line in range(9):
    current = [False] * 9

    for column in range(9):
        number = matriz_sudoku[line][column]
        current[number - 1] = True

    if False in current:
        line_error = line + 1
        break

# check the columns
for column in range(9):
    current = [False] * 9

    for line in range(9):
        number = matriz_sudoku[line][column]
        current[number - 1] = True

    if False in current:
        column_error = column + 1
        break

# check the 3x3 quadrants
for start_line in range(0, 9, 3):
    for start_column in range(0, 9, 3):
        current = [False] * 9

        for line in range(start_line, start_line + 3):
            for column in range(start_column, start_column + 3):
                number = matriz_sudoku[line][column]
                current[number - 1] = True

        if False in current:
            quadrant_error = ((start_line + start_column) // 3) + 1
            break

if line_error != -1:
    print(f"Has error on line {line_error}")

if column_error != -1:
    print(f"Has error on column {column_error}")

if quadrant_error != -1:
    print(f"Has error on quadrant {quadrant_error}")
