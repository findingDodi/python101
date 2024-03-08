import random


class MessageController:
    def __init__(self):
        self.messages = [
            "1. No one is perfect - that’s why pencils have erasers. - Wolfgang Riebe",
            "2. Have no fear of perfection - you'll never reach it. - Salvador Dali",
            "3. The tallest mountain started as a stone. - One Punch Man Intro",
            "4. Make it work. Make it nice. Make it fast. Always obey this order! - kiraa",
            "5. A good programmer is someone who always looks both ways before crossing a one-way street. – Doug Linder",
            "6. If debugging is the process of removing software bugs, then programming must be the process of putting them in. - Edsger W. Dijkstra"
        ]
        self.messages_shuffled = self.messages.copy()
        random.shuffle(self.messages_shuffled)
        self.message_index = 0

    # returned eine random Nachricht aus messages
    def get_random_message(self):
        random_number = random.randrange(len(self.messages))
        return self.messages[random_number]

    # returned eine random Nachricht aus messages_shuffled
    def get_next_random_message(self):
        random_message = self.messages_shuffled.pop(0)
        self.messages_shuffled.append(random_message)

        return random_message

    # Funktion mit Rekursion = böse
    # returned eine random Nachricht ohne Wiederholung
    def get_next_random_message_no_repeat_evil(self):
        if len(self.messages_shuffled) > 0:
            random_message = self.messages_shuffled.pop(0)
            return random_message
        else:
            self.messages_shuffled = self.messages.copy()
            random.shuffle(self.messages_shuffled)
            random_message = self.get_next_random_message_no_repeat_evil()
            return random_message

    # returned eine random Nachricht ohne Wiederholung
    def get_next_random_message_no_repeat(self):
        random_message = self.messages_shuffled[self.message_index]
        self.message_index += 1

        if self.message_index >= len(self.messages_shuffled):
            self.message_index = 0
            random.shuffle(self.messages_shuffled)

        return random_message
