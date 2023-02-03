import sys

# Aufgabe 02
# input für vorne oder hinten

DIRECTION_FRONT = 0
DIRECTION_BACK = 1

source_array = [5, 7, 3, 2, 1, 0, 8, 9, 4, 6]

print(source_array)
print('[{}]front [{}]back'.format(DIRECTION_FRONT, DIRECTION_BACK))
user_direction = int(input('From which direction would you like to sum up? '))

if user_direction != DIRECTION_FRONT and user_direction != DIRECTION_BACK:
    print('Please chose a valid direction!')
    sys.exit()

user_amount = int(input('How many numbers would you like to sum up? '))

if not 1 <= user_amount <= len(source_array):
    print('Your amount is out of range!')
    sys.exit()

print('Your chosen amount:', user_amount)
user_sum = 0

if user_direction == DIRECTION_FRONT:
    for i in range(user_amount):
        user_sum += source_array[i]

elif user_direction == DIRECTION_BACK:
    source_array.reverse()
    for i in range(user_amount):
        user_sum += source_array[i]

print('Your sum:', user_sum)
