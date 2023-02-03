# Aufgabe 01
from Member import Member


# gibt ein String-Array zurück mit 1 Zeile pro String (inkl \n)
def get_lines_from_file(file="Mitglieder.txt"):
    file_handle = open(file, "r")
    file_content = file_handle.readlines()
    file_handle.close()

    return file_content


def get_sanitized_string_array(string_array):
    cleaned_string_array = []
    for member_string in string_array:
        cleaned_string = member_string.replace("🐹", "").replace("  ", " ").rstrip()
        cleaned_string_array.append(cleaned_string)

    return cleaned_string_array


def get_member_set_from_array(string_array):
    member_list = []
    for member in string_array:
        single_member_array = member.split()
        if len(single_member_array) > 0:
            member_list.append(Member(single_member_array[0], int(single_member_array[1])))

    return member_list


def print_members():
    member_lines = get_lines_from_file()
    member_array = get_sanitized_string_array(member_lines)
    member_set = get_member_set_from_array(member_array)
    for member in member_set:
        print(member)


print_members()
