import random
import os


def get_number():
    chosen_number = 7
    current_modus = int(input("Enter Modus (0 for computer, 1 for multiplayer): "))

    if current_modus == 0:
        chosen_number = random.randint(1, current_span)
    elif current_modus == 1:
        chosen_number = int(input("Please enter number to guess (1-10): "))
        os.system('cls' if os.name == 'nt' else 'clear')

    return chosen_number


def save_highscore(name, user_score):
    score_info = [name.strip(), user_score]
    highscores.append(score_info)

    if len(highscores) > 1:
        sort_highscores()

    best_of_five = highscores[0:5]

    file_handle = open("highscores.txt", "w")

    for highscore in best_of_five:
        score_info = "{};{}\n".format(highscore[0], highscore[1])
        file_handle.write(score_info)

    file_handle.close()


def read_highscores():
    if not os.path.isfile("highscores.txt"):
        return

    file_handle = open("highscores.txt", "r")
    file_lines = file_handle.readlines()

    for line in file_lines:
        single_parts = line.rstrip().split(";")
        highscores.append([
            single_parts[0],
            int(single_parts[1])
        ])

    file_handle.close()


def sort_highscores():
    highscores.sort(key=lambda x: x[1], reverse=True)


def print_highscores():
    print("Here are the current Highscores:")
    for highscore in highscores:
        print("{}{}".format(highscore[0].ljust(20, " "), str(highscore[1]).rjust(3, " ")))
        print("#" * 20)


current_span = 10
current_tries = 3
current_score = 0
current_number = get_number()
highscores = []
keep_running = True

print("Welcome to numberGo!")
read_highscores()

while keep_running:

    print_highscores()

    print("You have 3 tries to guess the chosen number out of the range", current_span)

    while current_tries > 0:
        guess = int(input("Please enter your guess: "))

        if guess == current_number:
            print("Congrats! You guessed right!")
            print("The chosen number was", current_number)
            print("You needed", current_tries, "tries")
            break

        else:
            current_tries -= 1
            print("Sorry! Your guess was not correct")

            if current_tries == 0:
                print("You have no more guesses left")
                print("The number you needed to guess was", current_number)
                break

            if guess < current_number:
                print("The chosen number is greater than that!")

            if guess > current_number:
                print("The chosen number is smaller than that!")

            print("You have", current_tries, "left")

        print("#" * 10)

    if current_tries == 3:
        current_score += 3
    elif current_tries == 2:
        current_score += 2
    elif current_tries == 1:
        current_score += 1

    print("Your current score is", current_score)
    print("#" * 20)

    keep_going = int(input("Do you want to play another round (0 for no, 1 for yes)? "))
    if keep_going == 0:
        user_name = input("Please enter your name (max 20 chars): ")
        save_highscore(user_name, current_score)
        keep_running = False
    elif keep_going == 1:
        current_tries = 3
        current_number = get_number()
