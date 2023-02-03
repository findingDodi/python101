import itertools
import string

counter = 0
password = "zz"

for one_letter_password in itertools.product(string.ascii_lowercase):
    counter += 1
    check_password = ''.join(one_letter_password)

    if (counter % 500) == 0 or counter <= 27:
        print(check_password)

    if check_password == password:
        print("Congrats! The password is:", password)
        break

    if counter == 26:
        for two_letter_password in itertools.product(string.ascii_lowercase):
            counter += 1
            check_password = ''.join(two_letter_password)

            if (counter % 500) == 0 or counter <= 27:
                print(check_password)

            if check_password == password:
                print("Congrats! The password is:", password)
                break


