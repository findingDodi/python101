import random

counter = 0
width = int(input("Width: "))
height = int(input("Height: "))

if width < 1 or height < 1:
    import sys
    sys.exit("Geht nicht.")

randomNumber = random.randrange(width * height)

#Schleife für Zeilen
for i in range(width):
    #Schleife für Spalten
    for j in range(height):
        counter += 1
        if counter == randomNumber:
            print("*", end='')
        else:
            print("#", end='')
    print()
        

