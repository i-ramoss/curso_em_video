snacks = ["burguer", "juice", "pizza", "pudding"]

# lists are mutable
snacks[3] = "popsicle"

print("Snacks: ", snacks)

# add elements to the list
snacks.append("pudding") # add to the end
snacks.insert(2, "hot-dog") # add to any position

print("Snacks: ", snacks)

# remove elements to the list
del snacks[0] # remove element on 0 position
snacks.pop() # remove element on the last position, but you can pass any position inside the parenthesis
snacks.remove("juice") # remove element by value

print("Snacks: ", snacks)

print()
print("-" * 50)
print()
####################################################################################

# create list from range
values = list(range(4,11))

print("values", values)

# sort a list
values = [8, 2, 5, 4, 9, 3, 0]
values.sort()

print("values", values)

# sort in reverse a list
values.sort(reverse=True)

print("values (reverse)", values)

print()
print("-" * 50)
print()
####################################################################################

listA = [2, 3, 4, 7]
listB = listA # não é feito uma cópia, mas uma ligação, listA e listB estão apontando para o mesmo valor, assim, se eu alterar um valor em listB esse valor também será alterado em listA

listB[1] = 99

print(f"List A: {listA}")
print(f"List B: {listB}")

print()

# para copiar os dados de uma lista, sem realizar a ligação entre elas:
listA = [2, 3, 4, 7]
listB = listA[:]
listB[1] = 99

print(f"List A: {listA}")
print(f"List B: {listB}")