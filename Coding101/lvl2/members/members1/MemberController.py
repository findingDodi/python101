from Member import Member


class MemberController:

    def __init__(self):
        self.member_list = []
        self.fill_member_list_from_file()

    def fill_member_list_from_file(self, file="Mitglieder.txt"):
        file_handle = open(file, "r")
        file_content = file_handle.readlines()
        file_handle.close()

        cleaned_string_array = []
        for member_string in file_content:
            cleaned_string = member_string.replace("🐹", "").replace("  ", " ").rstrip()
            cleaned_string_array.append(cleaned_string)

        for member in cleaned_string_array:
            single_member_array = member.split()
            if len(single_member_array) > 0:
                self.member_list.append(Member(single_member_array[0], int(single_member_array[1])))

    def get_all_member_ids(self):
        all_member_ids = []
        for member in self.member_list:
            all_member_ids.append(member.get_member_id())

        return all_member_ids

    def get_random_member_id(self):
        all_member_ids = self.get_all_member_ids()
        random_id = 1
        while random_id in all_member_ids:
            random_id += 1

        return random_id

    def get_new_member(self, member_name):
        return Member(member_name, self.get_random_member_id())

    def add_member_to_member_list(self, member):
        self.member_list.append(member)

    def print_all_members(self):
        self.member_list.sort(key=lambda x: x.id)
        for member in self.member_list:
            print(member)

