from MemberController import MemberController

keep_running = True
my_member_controller = MemberController()

while keep_running:
    show_members = input("Do you want to see all Members? y/n ")
    if show_members == "y":
        my_member_controller.print_all_members()

    add_member = input("Do you want to add a new member? y/n ")
    if add_member == "y":
        new_member_name = input("Please type the name of the new member: ")
        my_member_controller.add_member_to_member_list(my_member_controller.get_new_member(new_member_name))
        print("Member was successfully added!")

    keep_swimming = input("Do you need to see or add members? y/n ")
    if keep_swimming != "y":
        keep_running = False
