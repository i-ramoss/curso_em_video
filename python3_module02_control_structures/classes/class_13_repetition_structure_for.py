for current in range(8, -1, -1):
    print(current, end=' ')

print("Exit")

start = int(input('Start: '))
end = int(input('End: '))
iterator = int(input('Iterator: '))

counter = 0

for current in range(start, end, iterator):
    print(current, end=' ')
    counter += current

print("Exit")
print("Counter: ", counter)

