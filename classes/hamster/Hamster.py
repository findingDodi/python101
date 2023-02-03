# Klassen fangen mit einem großen Buchstaben an
class Hamster:
    # Constructor
    # self als erster Parameter (ist die Klasse selbst)
    # self wird automatisch übergeben
    def __init__(self, name):
        self.name = name
        self.hunger = 50
        self.age = 0
        self.__alive = True

    def feed(self, amount):
        self.hunger -= amount
        if self.hunger < 0:
            self.__alive = False
            print(self.name, 'ist tot!')
        # self.hunger = self.hunger - amount

    def is_hungry(self):
        if self.hunger > 0:
            return True
        else:
            return False

    def on_fire(self):
        return False

    def is_alive(self):
        return self.__alive

    def run(self, distance):
        print(self.name, 'rennt eine Strecke von', distance, 'Metern')
        for i in range(distance):
            self.hunger += 1
        if self.hunger < 0 or self.hunger > 100:
            self.__alive = False
            print(self.name, 'ist tot!')
