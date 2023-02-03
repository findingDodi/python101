
class Member:

    def __init__(self, name, id):
        self.name = name
        self.id = id

    def __str__(self):
        member = self.name.ljust(10, " ") + str(self.id).rjust(3, " ")
        return member

    def __repr__(self):
        member = self.name.rjust(10, " ") + str(self.id).rjust(3, " ")
        return member

    def get_member_id(self):
        return self.id

