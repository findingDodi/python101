# do not try this at home!
import time


def do_sleep(sleepy_time):
    try:
        # time.sleep(sleepy_time)
        wake_up_time = time.time() + sleepy_time
        counter = 0
        while time.time() < wake_up_time:
            counter += 1
        print(counter)
    except KeyboardInterrupt:
        return False

    return True


for i in range(10):
    print(i)
    do_sleep(0.5)
