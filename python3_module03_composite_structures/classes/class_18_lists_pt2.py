people = list()

people = [["Ian Ramos", 45], ["Flora Ramos", 7], ["Cecília Ramos", 4]]

print(people[0][0]) # Ian
print(people[1][1]) # 7
print(people[2][0]) # "Cecília Ramos"
print(people[1]) # ["Flora Ramos", 7]

####################################################################################
print()
print("-" * 50)
print()
####################################################################################

somebody = list()

somebody.append("Jefferson")
somebody.append(28)

print("Somebody:", somebody)
print()

# copiar uma lista da forma correta:
guys = list()

# primeira forma
# somebody[0] = "Tiffany"
# somebody[1] = 33
# guys.append(somebody[:])

# segunda forma
guys.append(somebody.copy())

somebody[0] = "Tiffany"
somebody[1] = 33

guys.append(somebody.copy())

print("Guys:", guys)

####################################################################################
print()
print("-" * 50)
print()
####################################################################################

# para limpar os dados de uma lista é só utilizar a função .clear()

print(f"""
Antes do clear: {somebody}.
Retorno do clear: {somebody.clear()}
Depois do clear: {somebody}
""")

####################################################################################
print()
print("-" * 50)
print()
####################################################################################

items = ["a", "b", "c"]

# imprimir listas na ordem inversa

for item in reversed(items):
    print(item)