import random


def get_list_of_random_chars(random_char_amount, _width, _height):
    random_char_list = []

    # for i in range(randomCharAmount):
    #     randomNumber = random.randrange(width * height)
    #     if randomNumber not in randomCharList:
    #         randomCharList.append(randomNumber)

    # wir nutzen hier while, damit die liste wirklich bis zum Ende gefüllt wird
    while len(random_char_list) < random_char_amount:
        random_number = random.randrange(1, (_width * _height) + 1)
        if random_number not in random_char_list:
            random_char_list.append(random_number)

    return random_char_list


counter = 0
randomCharAmount = int(input("Zufallszahlenanzahl: "))
width = int(input("Width: "))
height = int(input("Height: "))
ausgabe = ""
ausgabeListe = []

if width < 1 or height < 1:
    import sys
    sys.exit("Geht nicht.")

# Verhinderung einer endlosen Schleife:
if randomCharAmount > (width * height):
    import sys
    sys.exit("Geht nicht.")

randomAmountCharList = get_list_of_random_chars(randomCharAmount, width, height)
print(randomAmountCharList)
# Schleife für Zeilen
for i in range(width):
    # Schleife für Spalten
    for j in range(height):
        counter += 1
        if counter in randomAmountCharList:
            print("*", end='')
            ausgabe += "*"
            ausgabeListe.append("*")
        else:
            print("#", end='')
            ausgabe += "#"
            ausgabeListe.append("#")

    # print()
print()
print(ausgabe)
print(ausgabeListe)
