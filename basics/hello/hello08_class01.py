from classes.hamster import Hamster

myHamster = Hamster.Hamster('Keks')

# gibt den return-Wert der Funktion zurück
print(myHamster.is_hungry())

# gibt die Funktion selbst zurück
print(myHamster.is_hungry)

# gibt die angesprochene Eigenschaft des Objekts zurück
print(myHamster.hunger)

feedHamster = int(input("Wie viel Futter willst du dem Hamster geben? "))
myHamster.feed(feedHamster)

if myHamster.is_hungry():
    print('Der Hamster ist noch zu', myHamster.hunger, '% hungrig')
    # feedHamster = int(input("Wie viel Futter willst du dem Hamster geben? "))
    # myHamster.feed(feedHamster)
    # print('Der Hamster ist noch zu' + myHamster.hunger + '% hungrig')
else:
    print('Der Hamster ist nicht hungrig')
