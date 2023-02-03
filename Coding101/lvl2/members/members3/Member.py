
class Member:
    HAMSTER_SEPARATOR = " 🐹 "

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

    def get_member_name(self):
        return self.name

    def get_save_string(self):
        return "{}{}{}\n".format(self.get_member_name(), Member.HAMSTER_SEPARATOR, self.get_member_id())
