# Write a programa that reads any angle and display on the screen a value of the sine, cosine, and tangent of that angle.
from math import sin, cos, tan, radians

angle = float(input('Enter a angle: '))

angle_in_radians = radians(angle)

print('The sine of {}º is {:.2f}, the cosine is {:.2f} and the tangent is {:.2f}'.format(angle, sin(angle_in_radians), cos(angle_in_radians), tan(angle_in_radians)))