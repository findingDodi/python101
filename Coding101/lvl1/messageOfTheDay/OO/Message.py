
class Message:
    def __init__(self, quote, author):
        self.quote = quote
        self.author = author
        self.read = False

    def get_message(self):
        return '{} - {}'.format(self.quote, self.author)

    def message_read(self):
        return self.read

