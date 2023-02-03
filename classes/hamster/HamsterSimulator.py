import random
import Hamster04 as Hamster
import time

myHamster = Hamster.Hamster('Sunny')

counterFood = 0
counterDistance = 0

while myHamster.is_alive():
    myHamster.aging()

    if myHamster.is_hungry() and myHamster.is_alive():
        food = random.randrange(1, 20)
        counterFood += food
        print(food)
        print("Hunger level:", myHamster.hunger)
        myHamster.feed(food)

    if myHamster.is_alive() == True:
        runDistance = random.randrange(1, 20)
        counterDistance += runDistance
        print(runDistance)
        print("Hunger level:", myHamster.hunger)
        myHamster.run(runDistance)

print(myHamster.name, "ist insgesamt", myHamster.age, "Jahre alt geworden.")
print(myHamster.name, "hat insgesamt", myHamster.time, "Sekunden gelebt.")
print(myHamster.name, "hat insgesamt", counterFood, "gegessen.")
print(myHamster.name, "ist insgesamt", counterDistance, "gerannt.")
