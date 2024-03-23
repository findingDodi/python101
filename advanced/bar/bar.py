
in_bar = True
drinks_in_stock = ["Beer", "Wine", "Water"]
round_counter = 0

print('Welcome to Drink Barrymore! How can i help you?')

while in_bar:

    if round_counter > 0:
        user_stays = input('Would you like another round (y/n)? ')
        if user_stays != 'y':
            print('See you in a while, crocodile!')
            in_bar = False
            continue

    print('Here is what we have in stock:')

    for drink in drinks_in_stock:
        print(drink)

    user_drink = input('What drink would you like to order? ')

    if 'bathroom' in user_drink:
        print('🔥🔥🔥💀💀🔥🔥🔥')
        in_bar = False
        continue

    if user_drink not in drinks_in_stock:
        print('Try to order something from the menu next time ;)')
        continue

    user_drink_amount = int(input('How many drinks would you like? '))

    if user_drink_amount < 0:
        print('So you would like to give me a drink?')
    elif user_drink_amount == 0:
        print('Okaaay I come around another time!')
    else:
        print('Here you go', user_drink_amount, user_drink)

    round_counter += 1
    print('#' * 10)
    print('Time for a new round of drinks!')
