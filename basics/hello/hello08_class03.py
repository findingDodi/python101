from classes.hamster import Hamster

myHamster = Hamster.Hamster('Keks')

while myHamster.is_alive() == True:

    if myHamster.is_hungry() == True:
        print(myHamster.name, 'ist noch zu', myHamster.hunger, '% hungrig')
        hamsterFeed = int(input("Wie viel Futter willst du " + myHamster.name + " geben? "))
        myHamster.feed(hamsterFeed)

    if myHamster.is_alive() == True:
        print(myHamster.name, 'ist noch zu', myHamster.hunger, '% hungrig')
        hamsterRun = int(input("Wie viele Meter soll " + myHamster.name + " rennen? "))
        myHamster.run(hamsterRun)

if myHamster.is_hungry() == False and myHamster.is_alive() == True:
    print(myHamster.name, 'ist nicht mehr hungrig!')
