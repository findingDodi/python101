import random
import os
import time

height = 4
width = 10
inner_width = width - 2

other_lines = "#" + " " * inner_width + "#"
bottom_line = "#" * width
tetris_content = []

for i in range(height):
    tetris_content.append(list(other_lines))
tetris_content.append(list(bottom_line))

current_level = 0
current_slot = random.randrange(1, 9)

while current_level < height:
    os.system('cls' if os.name == 'nt' else 'clear')
    tetris_content[current_level][current_slot] = "*"

    for i in range(len(tetris_content)):
        print("".join(tetris_content[i]))

    tetris_content[current_level][current_slot] = " "
    current_level += 1

    time.sleep(0.5)

