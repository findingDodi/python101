import random
import os


def get_random_number(span):
    return random.randint(1, span)


def get_number():
    current_number = 7
    current_modus = int(input("Enter Modus (0 for computer, 1 for multiplayer): "))
    if current_modus == 0:
        current_number = get_random_number(current_span)
    elif current_modus == 1:
        current_number = int(input("Please enter number to guess (1-10): "))
        os.system('cls' if os.name == 'nt' else 'clear')
    return current_number


current_span = 10
current_tries = 3
current_random_number = get_number()
keep_running = True
score = 0

print("Welcome to numberGo!")

while keep_running:

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

    if current_tries == 3:
        score += 3
    elif current_tries == 2:
        score += 2
    elif current_tries == 1:
        score += 1

    print("Your current score is", score)

    keep_going = int(input("Do you want to play another round (0 for no, 1 for yes)? "))
    if keep_going == 0:
        keep_running = False
    elif keep_going == 1:
        current_tries = 3
        current_random_number = get_number()
