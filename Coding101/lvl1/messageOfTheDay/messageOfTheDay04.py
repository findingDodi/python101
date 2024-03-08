from OO.MessageController import MessageController

new_message_controller = MessageController()


def printRandomMessage():
    keep_running = True

    while keep_running:
        user_input = input("Spielt den selben Song nochmal? y/n ")

        if user_input == "y":
            print(new_message_controller.getNextRandomMessageNoRepeat())
        else:
            keep_running = False


printRandomMessage()
