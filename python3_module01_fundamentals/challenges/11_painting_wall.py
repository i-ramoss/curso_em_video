# Make a program that reads the width and height of a wall in meters, calculates its area and the amount of paint needed to paint it, knowing that each liter of paint paints an area of 2 square meters.

width = float(input('Enter the width of the wall in meters: '))
height = float(input('Enter the height of the wall in meters: '))

area = width * height
square_meters_per_linter_of_paint = 2

print('You need {}L of paint to paint the {:.2f} square meters of wall.'.format(area // square_meters_per_linter_of_paint, area))