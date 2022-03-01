# Develop a logic that reads a person's weight and height, calculates their BMI
# and displays their status, according to the table below.

# Below 18.5: Underweight
# Between 18.5 and 25: Ideal weight
# Between 25 and 30: Overweight
# Above 40: Morbid obesity

weight = float(input('Enter here your weight (in kg): '))
height = float(input('Enter here your height (in cm): '))

bmi = weight * 10000 / pow(height, 2)

if (bmi < 18.5): print('Your BMI is: {:.1f}kg/m², you are underweight.'.format(bmi))

elif (18.5 <= bmi < 25): print('Your BMI is: {:.1f}kg/m², your weight is ideal'.format(bmi))

elif (25 <= bmi < 30): print('Your BMI is: {:.1f}kg/m², you are overweight.'.format(bmi))

elif (30 <= bmi < 40): print('Your BMI is: {:.1f}kg/m², you are obese.'.format(bmi))

else: print('Your BMI is: {:.1f}kg/m², you are morbidly obese'.format(bmi))