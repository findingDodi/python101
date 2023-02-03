# TestProgram Aufgabe 1-3

def print_numbers(amount):
    for i in range(1, amount + 1):
        print(i)


def write_every_fifth_element_into_file(amount=99, file="testProgram.txt"):
    file_handle = open(file, "w")

    for i in range(1, amount + 1):
        if i % 5 == 0:
            file_handle.write(str(i) + "\n")

    file_handle.close()


user_age = int(input("Please enter your age: "))
if user_age >= 18:
    print_numbers(999)
    write_every_fifth_element_into_file()
else:
    print("Scusi too young")
