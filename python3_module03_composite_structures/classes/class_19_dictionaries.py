people = {"name": "Ian Ramos", "sex": "M", "age": 23}

print(f'{people["name"]} have {people["age"]} years.')

print(people.keys())
print(people.values())
print(people.items())

####################################################################################
print()
print("-" * 50)
print()
####################################################################################


state = {"uf": "Bahia", "acronym": "BA"}
state2 = {"uf": "São Paulo", "acronym": "SP"}

brazil = [state, state2]

new_state = dict()

for _ in range(2):
    new_state["uf"] = str(input("Federative Unit: ")).strip()
    new_state["acronym"] = str(input("State Acronym: ")).strip()

    print()

    brazil.append(new_state.copy())

for states in brazil:
    for state_value in states.values():
        print(state_value, end="  ")
    print()

# print(f"Brazil: {brazil}")
