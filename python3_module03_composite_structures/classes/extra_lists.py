# Esses códigos não fazem parte do conteúdo disponibilizado pelo Curso em Vídeo

# criar uma sublista somente com números pares
# all = map(int, input().split())
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# forma tradicional
even = []

for number in numbers:
    if number % 2 == 0:
        even.append(number)
    
print("Even:", even)

# usando list comprehensions
even2 = [number for number in numbers if number % 2 == 0]

print("Even 2:", even2)