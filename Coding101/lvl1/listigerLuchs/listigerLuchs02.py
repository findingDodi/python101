# Aufgabe 02
# input für vorne oder hinten

source_array = [5, 7, 3, 2, 1, 0, 8, 9, 4, 6]

print(source_array)
print('[0]front [1]back')
user_direction = int(input('From which direction would you like to sum up? '))
user_amount = int(input('How many numbers would you like to sum up? '))
print('Your chosen amount:', user_amount)

if user_direction == 0 or user_direction == 1:
    if 1 <= user_amount <= len(source_array):
        user_sum = 0
        if user_direction == 0:
            for i in range(user_amount):
                user_sum += source_array[i]

        elif user_direction == 1:
            source_array.reverse()
            for i in range(user_amount):
                user_sum += source_array[i]

        print('Your sum:', user_sum)
    else:
        print('Your amount is out of range!')
else:
    print('Please chose a given direction!')
