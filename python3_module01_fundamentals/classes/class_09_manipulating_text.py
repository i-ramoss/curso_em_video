text = "Course In Video"

# Slicing

print(text[10:15:2])

# Analysis

print(len(text))
print(text.count("o"))
print(text.find("deo"))
print(text.find("life"))
print("Course" in text)

# Transformation

print(text.replace("Video", "MacOS"))
print(text.upper())
print(text.lower())
print(text.capitalize())
print(text.title())

text = "   Learn Python   "

print(text.strip())
print(text.rstrip())
print(text.lstrip())

# Division

print(text.split())
print(text.split()[1][0])

# Join

print("-".join(text))


print(
    """Welcome!
Are you completely new to programming?"""
)
