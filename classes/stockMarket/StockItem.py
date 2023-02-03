
class StockItem:

    def __init__(self, index, amount, name):
        self.index = int(index)
        self.amount = int(amount)
        self.name = name
        self.__presentation = self.name.ljust(10, " ") + str(self.amount).rjust(3, " ")

    def __str__(self):
        return self.__presentation

    def __repr__(self):
        return self.__presentation

    def get_name(self):
        return self.name

    def get_amount(self):
        return self.amount

    def get_index(self):
        return self.index

    def set_index(self, index):
        self.index = index

    def set_amount(self, amount):
        self.amount = amount

    def set_name(self, name):
        self.name = name
