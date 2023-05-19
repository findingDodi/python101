
class Printy:
    def __init__(self, text=""):
        self.text = text

    def do_print(self):
        print(self.text)

    def __repr__(self):
        return self.text
