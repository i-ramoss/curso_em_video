# Write a program that displays a coutdown to the burst of fireworks on the screen,
# going from 10 to 0, with a 1 second pause between them.

from time import sleep

for second in range(10, -1, -1):
    print(second)
    sleep(1)

print("Time is over! 🎆🎆🎆🎆")
