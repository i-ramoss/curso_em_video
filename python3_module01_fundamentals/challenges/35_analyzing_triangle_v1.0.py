# Develop a program that reads the length of tree lines and tells the user whether or not they can form a triangle

segment01 = int(input("Enter the first segment: "))
segment02 = int(input("Enter the second segment: "))
segment03 = int(input("Enter the third segment: "))

if (
    ((segment01 + segment02) > segment03)
    & ((segment02 + segment03) > segment01)
    & ((segment01 + segment03) > segment02)
):
    print("The triangle can be formed!")

else:
    print("The triangle can't be formed!")
