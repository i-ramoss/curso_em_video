# Write a programa that reads a value in meters and displays it converted to centimeters and millimeters

meter = int(input("Enter a value in meter: "))

print(
    "{} meters is equal to {} centimeters and {} millimeters".format(
        meter, meter * 100, meter * 1000
    )
)
