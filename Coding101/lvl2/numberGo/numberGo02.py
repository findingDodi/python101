import random
import os


def get_random_number(span):
    return random.randint(1, span)


def get_modus():
    return int(input("Enter Modus (0 for computer, 1 for multiplayer): "))


current_span = 10
current_tries = 3
current_random_number = 0
current_modus = get_modus()

if current_modus == 0:
    current_random_number = get_random_number(current_span)
elif current_modus == 1:
    current_random_number = int(input("Please enter number to guess (1-10): "))
    os.system('cls' if os.name == 'nt' else 'clear')

print("Welcome to numberGo!")
print("You have 3 tries to guess the chosen number out of the range", current_span)

while current_tries > 0:
    guess = int(input("Please enter your guess: "))

    if guess == current_random_number:
        print("Congrats! You guessed right!")
        print("The chosen number was", current_random_number)
        print("You needed", current_tries, "tries")
        break

    else:
        current_tries -= 1
        print("Sorry! Your guess was not correct")

        if current_tries == 0:
            print("You have no more guesses left")
            print("The number you needed to guess was", current_random_number)
            break

        if guess < current_random_number:
            print("The chosen number is greater than that!")

        if guess > current_random_number:
            print("The chosen number is smaller than that!")

        print("You have", current_tries, "left")
