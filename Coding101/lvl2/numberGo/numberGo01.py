import os

current_span = 10
current_tries = 3
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
