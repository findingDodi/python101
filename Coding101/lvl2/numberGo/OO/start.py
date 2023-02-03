from TheRound import TheRound
from TheHighscore import TheHighscore

my_highscore = TheHighscore()
separator = 20 * "#"
current_score = 0
keep_running = True

print("Welcome to numberGo!")

while keep_running:

    my_round = TheRound()
    my_round.set_modus(int(input("Enter Modus (1 for singleplayer, 2 for multiplayer): ")))
    if my_round.is_multiplayer():
        my_round.set_number(int(input("Enter Modus (1 for singleplayer, 2 for multiplayer): ")))

    my_highscore.print_highscores()

    print("You have", my_round.get_tries(), "tries to guess the chosen number out of the range", my_round.get_number_span())

    while my_round.are_tries_left():
        my_round.set_guess(int(input("Please enter your guess: ")))

        if my_round.is_guess_right():
            my_round.print_guess_right()
            break

        else:
            my_round.decrement_tries()
            print("Sorry! Your guess was not correct")

            if not my_round.are_tries_left():
                print("You have no more guesses left")
                print("The number you needed to guess was", my_round.number)
                break

            my_round.print_hint()

            print("You have", my_round.tries, "left")

        print(separator)

    current_score += my_round.get_points_for_tries()

    print("Your current score is", current_score)
    print(separator)

    keep_going = int(input("Do you want to play another round (0 for no, 1 for yes)? "))
    if keep_going != 1:
        user_name = input("Please enter your name (max 20 chars): ")
        my_highscore.save_highscore(user_name, current_score)
        keep_running = False
