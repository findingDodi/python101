from datetime import datetime

user_name = "hamster"
user_password = "test"
menu = ["1) Kochrezepte", "2) Weltherrschaft", "3) Uhrzeit", "q) Beenden"]
login_counter = 3
keep_running = True


def quit_program():
    global keep_running
    print("Program is now shutting down...")
    keep_running = False


while keep_running:
    if not login_counter <= 0:
        print("You have", login_counter, "tries to login")
        user_name_input = input("Please enter username: ")
        user_password_input = input("Please enter password: ")
        login_counter -= 1

        if user_name_input == user_name and user_password_input == user_password:

            user_decision_input = ""

            while user_decision_input != "q":
                for i in range(len(menu)):
                    print(menu[i])

                user_decision_input = input("Please choose an item from the menu: ")

                if user_decision_input == "1":
                    print("Sorry, there are no recipes available at the moment.")
                elif user_decision_input == "2":
                    print("Congrats! You are now the sole ruler of this called earth!")
                elif user_decision_input == "3":
                    print(datetime.now().strftime("%H:%M:%S"))
                else:
                    print("Try harder next time!")
                    quit_program()

    else:
        print("Sorry you have now no more tries to login!")
        quit_program()
