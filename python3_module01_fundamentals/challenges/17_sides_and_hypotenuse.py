# Write a program that reads the length of the opposite and adjacent sides of a right triangle, calculate and display the length of the hypotenuse

from math import hypot

opposite_side = float(input("Enter the opposite side: "))
adjacent_side = float(input("Enter the adjacent side: "))

print(
    "The hypotenuse of the right triangle formed by opposite side {:.1f} and adjacent side {:.1f} is {:.1f}".format(
        opposite_side, adjacent_side, hypot(opposite_side, adjacent_side)
    )
)
