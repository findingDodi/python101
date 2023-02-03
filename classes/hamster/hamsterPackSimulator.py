import random
import string
import Hamster04 as Hamster


def get_random_name(amount):
    output = ''
    letters_numbers = string.ascii_uppercase + string.digits
    for _ in range(amount):
        output += random.choice(letters_numbers)

    return output


def hamster_life_bak(hamsters):
    while hamsters.is_alive():
        hamsters.aging()

        if hamsters.is_hungry() and hamsters.is_alive():
            food = random.randrange(1, 20)
            hamsters.feed(food)

        if hamsters.is_alive() == True:
            run_distance = random.randrange(1, 20)
            hamsters.run(run_distance)


def hamster_life(hamsters):
    if hamsters.is_alive():
        hamsters.aging()

        if hamsters.is_hungry() and hamsters.is_alive():
            food = random.randrange(1, 20)
            hamsters.feed(food)

        if hamsters.is_alive() == True:
            run_distance = random.randrange(1, 20)
            hamsters.run(run_distance)


def is_any_hamster_alive(hamster_list):
    hamsters_alive = 0
    for _hamster in hamster_list:
        if _hamster.is_alive():
            hamsters_alive += 1

    return hamsters_alive > 0


hamster = None
hamster_array = []
hamster_amount = 5

for i in range(hamster_amount):
    name = get_random_name(5)
    hamster = Hamster.Hamster(name)
    hamster_array.append(hamster)
    #hamster_life(hamster)

#for i in range(len(hamster_array)):
    #hamster_life(hamster_array[i])

while is_any_hamster_alive(hamster_array):
    print('#' * 15)
    for _hamster in hamster_array:
        hamster_life(_hamster)

#print(hamster_array)
