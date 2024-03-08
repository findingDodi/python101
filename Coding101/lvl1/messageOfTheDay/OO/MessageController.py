from Message import Message
from typing import List
import random


class MessageController:

    def __init__(self):
        self.messages: List[Message] = []

    def add_message(self, quote, author):
        self.messages.append(Message(quote, author))

    def get_random_message(self):
        # TODO: figure out how to filter list
        # unread_messages: List[Message] = filter(message_read(), self.messages)
        random_message: Message = random.choice(self.messages)

