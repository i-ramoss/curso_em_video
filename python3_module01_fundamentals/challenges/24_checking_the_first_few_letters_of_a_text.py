# Create a program that reads the name of a city and tells you whether or not starts with the name "Santo"

city = str(input("Enter a city name: ")).strip()

print("santo" in city[:6].lower())
