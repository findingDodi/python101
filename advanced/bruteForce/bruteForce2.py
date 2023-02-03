import itertools
import string

password = "hamst"


def brute_force(repeat):
    counter = 0
    max_repeat = 26 ** repeat
    for one_letter_password in itertools.product(string.ascii_lowercase, repeat=repeat):
        counter += 1
        check_password = ''.join(one_letter_password)

        if (counter % 1000000) == 0 or counter == 1:
            print(check_password, len(check_password))

        if check_password == password:
            print("Congrats! The password is:", password)
            break

        if counter == max_repeat:
            brute_force(repeat+1)


brute_force(1)
