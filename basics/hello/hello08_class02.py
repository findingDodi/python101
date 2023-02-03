from classes.hamster import Hamster

myHamster = Hamster.Hamster('Keks')

# feedHamster = int(input("Wie viel Futter willst du dem Hamster geben? "))
# myHamster.feed(feedHamster)

while myHamster.is_hungry():
    print(myHamster.name, 'ist noch zu', myHamster.hunger, '% hungrig')
    feedHamster = int(input("Wie viel Futter willst du dem Hamster geben? "))
    myHamster.feed(feedHamster)

if myHamster.is_hungry() == False and myHamster.is_alive() == True:
    print(myHamster.name, 'ist nicht mehr hungrig!')
