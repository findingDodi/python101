# Aufgabe 01
# Array lesbar ausgeben, input amount sum, summe ausgeben

source_array = [5, 7, 3, 2, 1, 0, 8, 9, 4, 6]

print(source_array)
user_amount = int(input('How many numbers would you like to sum up? '))
print('Your chosen amount:', user_amount)

if 1 <= user_amount <= len(source_array):
    user_sum = 0

    for i in range(user_amount):
        user_sum += source_array[i]

    print('Your sum:', user_sum)
else:
    print('Your amount is out of range!')
