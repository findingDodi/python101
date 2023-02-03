import random

counter = 0
randomNumber = random.randrange(25)
print(randomNumber)

#Schleife für Zeilen
for i in range(5):
    #Schleife für Spalten
    for j in range(5):
        if counter == randomNumber:
            print("*", end='')
        else:
            print("#", end='')

        counter += 1

    print()
        
