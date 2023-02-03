# TestProgram Aufgabe 4+5 (incl 1-3)

def print_numbers(amount):
    for i in range(1, amount + 1):
        print(i)


def write_every_fifth_element_into_file(amount=99, file="testProgram.txt"):
    file_handle = open(file, "w")

    for i in range(1, amount + 1):
        if i % 5 == 0:
            file_handle.write(str(i) + "\n")

    file_handle.close()


def write_words_into_file(text, file_name, file_extension):
    file = file_name + "." + file_extension
    file_handle = open(file, "w")
    file_handle.write(text)
    file_handle.close()


user_age = int(input("Please enter your age: "))
if user_age >= 18:
    user_name = input("Please enter your username: ")
    user_password = input("Please enter your password: ")

    while user_name != "hamster" or user_password != "hamster":
        print("Please try again... something seems to be wrong")
        user_name = input("Please enter your username: ")
        user_password = input("Please enter your password: ")

    print_numbers(999)
    write_every_fifth_element_into_file()

    print("Now you have the opportunity to save a text to a file:")
    user_text = input("Please enter your text: ")
    user_file_name = input("Please enter your filename: ")
    user_file_extension = input("Please enter your file extension: ")
    write_words_into_file(user_text, user_file_name, user_file_extension)

else:
    print("Scusi too young")
