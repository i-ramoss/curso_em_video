# Esses códigos não fazem parte do conteúdo disponibilizado pelo Curso em Vídeo

# inicialização de uma matriz zerada (todos os elementos iguais a 0)
lines = 3
columns = 4

matriz = []

## inserindo elementos um a um
# for line in range(lines):
#     lineList = []

#     for column in range(columns):
#         lineList.append(0)

#     matriz.append(lineList)

# print(matriz)


## inserindo linha a linha
# for _ in range(lines):
#     matriz.append([0] * columns)

# print(matriz)


## list comprehension:
# matriz = [[0] * columns for _ in range(lines)]

# print(matriz)

####################################################################################
print()
print("-" * 50)
print()
####################################################################################

# Função para criar uma matriz zerada, mas que recebe linhas e colunas como parâmetros
# def matriz(lines, columns):
#     newMatriz = []

#     for _ in range(lines):
#         newMatriz.append([0] * columns)

#     return newMatriz

# print(matriz(int(input("Número de linhas: ")), int(input("Número de colunas: "))))

####################################################################################
print()
print("-" * 50)
print()
####################################################################################

# Criando uma matriz a partir de dados da entrada
line, columns = [int(entry) for entry in input().split()]

# matriz = []

### uma possibilidade (não parece ser a melhor implementação pois não respeita os dados de entrada)
# for _ in range(line):
#     matriz.append([int(value) for value in input().split()])

### outra possibilidade (não parece ser a melhor implementação pois não respeita os dados de entrada)
matriz = [[int(value) for value in input().split()] for _ in range(line)]

print("Matriz:", matriz)
