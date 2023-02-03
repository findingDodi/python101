from Member import Member


class MemberController:

    def __init__(self, member_file="Mitglieder.txt"):
        self.member_list = []
        self.max_member_id = -1
        self.member_file = member_file

        self.fill_member_list_from_file(member_file)

    def fill_member_list_from_file(self, file):
        self.member_file = file
        file_handle = open(file, "r")
        file_content = file_handle.readlines()
        file_handle.close()

        members_array = []
        for member_string in file_content:
            cleaned_member_array = member_string.rstrip().split(" 🐹 ")
            members_array.append(cleaned_member_array)

        for single_member_array in members_array:
            if len(single_member_array) > 1:
                _current_member_id = int(single_member_array[1])
                if _current_member_id > self.max_member_id:
                    self.max_member_id = _current_member_id
                self.member_list.append(Member(single_member_array[0], _current_member_id))

    def get_next_member_id(self):
        next_member_id = self.max_member_id + 1
        return next_member_id

    def add_member(self, member_name):
        member = Member(member_name, self.get_next_member_id())
        self.member_list.append(member)
        self.max_member_id = member.get_member_id()

    def print_all_members(self):
        self.member_list.sort(key=lambda x: x.id)
        for member in self.member_list:
            print(member)

    def save(self):
        file = "members.txt"
        file_handle = open(file, "w")
        file_input = ""

        for member in self.member_list:
            file_input += member.get_save_string()

        file_handle.write(file_input)
        file_handle.close()

