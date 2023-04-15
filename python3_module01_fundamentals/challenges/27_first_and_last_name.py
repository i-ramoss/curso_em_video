# Make a programa that reads a persons's full name, then display their first and last name separately.

full_name = str(input("Enter your full name: ")).strip()

splitted_full_name = full_name.split()

print("Your first name is {}!".format(full_name.split()[0]))
print(
    "And your last name is {}!".format(splitted_full_name[len(splitted_full_name) - 1])
)
