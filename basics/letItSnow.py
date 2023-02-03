import time

keep_running = True
time_to_sleep = 0.5
left = "* " * 10
right = " *" * 10
jiggle = True


def do_sleep(sleepy_time):
    try:
        time.sleep(sleepy_time)
    except KeyboardInterrupt:
        return False

    return True


while keep_running:
    if jiggle:
        print(left)
    else:
        print(right)

    keep_running = do_sleep(time_to_sleep)
    jiggle = not jiggle
