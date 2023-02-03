import sys

# Aufgabe 03
# array sortieren

DIRECTION_FRONT = 0
DIRECTION_BACK = 1
ARRAY_UNSORT = 0
ARRAY_SORT = 1

source_array = [5, 7, 3, 2, 1, 0, 8, 9, 4, 6]


def sum_up(amount):
    array_sum = 0
    for i in range(amount):
        array_sum += source_array[i]
    return array_sum


# Program
print(source_array)

print('[{}]no [{}]yes'.format(ARRAY_UNSORT, ARRAY_SORT))
user_sorting = int(input('Would you like to sort the array before summing up? '))

if user_sorting != ARRAY_SORT and user_sorting != ARRAY_UNSORT:
    print('Please chose a valid sorting!')
    sys.exit()

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

if user_sorting == ARRAY_SORT:
    source_array.sort()

if user_direction == DIRECTION_FRONT:
    user_sum = sum_up(user_amount)

elif user_direction == DIRECTION_BACK:
    source_array.reverse()
    user_sum = sum_up(user_amount)

print('Your sum:', user_sum)
