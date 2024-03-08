from OO.MessageController import MessageController

new_message_controller = MessageController()


def print_random_message():
    keep_running = True

    while keep_running:
        user_input = input("Spielt den selben Song nochmal? y/n ")

        if user_input == "y":
            print(new_message_controller.getNextRandomMessageNoRepeat())
        else:
            keep_running = False


print_random_message()
