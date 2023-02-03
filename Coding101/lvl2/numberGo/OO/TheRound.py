import random
from Modus import Modus


class TheRound:

    def __init__(self, tries=3):
        self.tries = tries
        self.number_span = 10
        self.guess = 0

        self.modus = Modus.NOT_SET

        self.number = -1
        self.set_number()

    def set_modus(self, modus):
        if modus == Modus.SINGLEPLAYER:
            self.modus = Modus.SINGLEPLAYER
        elif modus == Modus.MULTIPLAYER:
            self.modus = Modus.MULTIPLAYER
        else:
            self.modus = Modus.SINGLEPLAYER

    def set_number(self, number=None):
        if self.modus == Modus.SINGLEPLAYER:
            self.number = random.randint(1, self.number_span)
        elif self.modus == Modus.MULTIPLAYER:
            self.number = number

    def set_guess(self, guess):
        self.guess = guess

    def get_tries(self):
        return self.tries

    def get_number(self):
        return self.number

    def get_number_span(self):
        return self.number_span

    def get_points_for_tries(self):
        if self.get_tries() == 3:
            return 3
        elif self.get_tries() == 2:
            return 2
        elif self.get_tries() == 1:
            return 1

        return 0

    def decrement_tries(self):
        self.tries -= 1

    def is_multiplayer(self):
        if self.modus == Modus.MULTIPLAYER:
            return True

        return False

    def is_guess_right(self):
        if self.guess == self.number:
            return True

        return False

    def are_tries_left(self):
        if self.tries == 0:
            return False

        return True

    def print_guess_right(self):
        print("Congrats! You guessed right!")
        print("The chosen number was", self.number)
        print("You needed", self.tries, "tries")

    def print_hint(self):
        if self.guess < self.number:
            print("The chosen number is greater than that!")

        if self.guess > self.number:
            print("The chosen number is smaller than that!")
