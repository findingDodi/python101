import time

input_number = int(input("Enter max Wave Length: "))
time_to_sleep = 0.5
hashtag = "#"
fill = " "


def get_output_string(length):
    return hashtag.rjust(length, fill)


def do_sleep(sleepy_time):
    try:
        time.sleep(sleepy_time)
    except KeyboardInterrupt as ex:
        # print("Keyboard: ", ex)
        return False

    return True


keep_running = True

while keep_running:
    keep_swimming = True
    if input_number >= 1:
        for i in range(input_number + 1):
            if not do_sleep(time_to_sleep):
                keep_swimming = False
            print(get_output_string(i+1))

        for i in range(input_number, 1, -1):
            if not do_sleep(time_to_sleep):
                keep_swimming = False
            print(get_output_string(i))

        keep_running = keep_swimming

print(hashtag)
