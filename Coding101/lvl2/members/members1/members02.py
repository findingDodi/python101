# Aufgabe 02+03
# TODO: MemberController
import random
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


def get_member_list_from_array(string_array):
    member_list = []
    for member in string_array:
        single_member_array = member.split()
        if len(single_member_array) > 0:
            member_list.append(Member(single_member_array[0], int(single_member_array[1])))

    return member_list


def get_member_list_from_file():
    member_lines = get_lines_from_file()
    member_array = get_sanitized_string_array(member_lines)
    member_list = get_member_list_from_array(member_array)

    return member_list


def get_all_member_ids():
    member_list = get_member_list_from_file()
    member_ids = set()
    for member in member_list:
        member_ids.add(member.get_member_id())

    return member_ids


def get_random_member_id():
    all_member_ids = get_all_member_ids()
    random_id = 1
    while random_id in all_member_ids:
        random_id += 1

    return random_id


def get_new_member(new_member_name):
    return Member(new_member_name, get_random_member_id())


def print_members(member_list):
    member_list.sort(key=lambda x: x.id)
    for member in member_list:
        print(member)


all_members = get_member_list_from_file()

keep_running = True

while keep_running:
    show_members = input("Do you want to see all Members? y/n ")
    if show_members == "y":
        print_members(all_members)
        add_member = input("Do you want to add a new member? y/n ")
        if add_member == "y":
            new_member_name = input("Please type the name of the new member: ")
            all_members.append(get_new_member(new_member_name))
            print("Member was successfully added!")
        else:
            keep_running = False

    else:
        keep_running = False
