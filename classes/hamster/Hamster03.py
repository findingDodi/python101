
class Hamster:
    # Konstruktor
    # self als erster Parameter (ist die Klasse selbst, Äquivalent in Java: this)
    # self wird automatisch übergeben
    def __init__(self, name):
        self.name = name
        self.hunger = 50
        self.age = 0
        self.death_reason = ""
        self.__alive = True

    def feed(self, amount):
        self.hunger -= amount
        self.try_kill_hamster()
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

    # Hamster soll eine bestimmte Distanz laufen
    # Funktion benutzen, auswählbar zwischen laufen und füttern
    def run(self, distance):
        print(self.name, "rennt eine Strecke von", distance, "Metern.")
        
        # Das Hunger-Level soll basierend auf der Distanz erhöht werden
        self.hunger += distance
            
        self.try_kill_hamster()

    def try_kill_hamster(self):
        if not self.is_alive():
            return

        self.kill_hamster(self.hunger < 0, "Unterfütterung")
        self.kill_hamster(self.hunger > 100, "Überfütterung")
        self.kill_hamster(self.age > 50, "Altersschwäche")

        '''
        if self.hunger < 0 or self.hunger > 100:
            self.kill_hamster("Über-/Unterfütterung")

        if self.age > 50:
            self.kill_hamster("Altersschwäche")
        '''

    def kill_hamster(self, has_died, death_reason):
        if not self.is_alive() or not has_died:
            return

        self.__alive = False
        self.death_reason = death_reason
        print(self.name, "ist an", self.death_reason, "gestorben.")

    def aging(self):
        self.age += 1
        
        self.try_kill_hamster()
