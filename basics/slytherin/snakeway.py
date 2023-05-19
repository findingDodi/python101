import time

START = "╞"
END = "╡"
HORIZONTAL = "═"
VERTICAL = "║"
RIGHT_DOWN = "╗"
RIGHT_LEFT = "╝"
LEFT_DOWN = "╔"
LEFT_RIGHT = "╚"
SPACE = " "

STEPS_HORIZONTAL = 10
STEPS_VERTICAL = 2


def do_sleep(sleepy_time):
    try:
        time.sleep(sleepy_time)
    except KeyboardInterrupt:
        return False

    return True


def to_the_right(is_start):
    for i in range(STEPS_HORIZONTAL):
        if i == 0 and is_start:
            print(START, end="")
        elif i == 0 and not is_start:
            print(LEFT_RIGHT, end="")
        if i > 0 and i < 9:
            print(HORIZONTAL, end="")
        if i == 9:
            print(RIGHT_DOWN)

        do_sleep(time_to_sleep)


def right_to_the_bottom():
    for i in range(STEPS_VERTICAL):
        print(SPACE * 9 + VERTICAL)
        do_sleep(time_to_sleep)


def to_the_left():
    for i in range(STEPS_HORIZONTAL - 1, 0, -1):
        if i == (STEPS_HORIZONTAL - 1):
            print(SPACE * 9 + RIGHT_LEFT, end="", flush=True)
        if i > 0 and i < 9:
            spaces = SPACE * (i - 1)
            horizontals = HORIZONTAL * (STEPS_HORIZONTAL - i)
            print(spaces + horizontals + RIGHT_LEFT, end="", flush=True)

        do_sleep(time_to_sleep)
        print("\33[1D\r", end="", flush=True)

    print(LEFT_DOWN + HORIZONTAL * (STEPS_HORIZONTAL - 2) + RIGHT_LEFT)


def left_to_the_bottom():
    for i in range(STEPS_VERTICAL):
        print(VERTICAL + SPACE * 9)
        do_sleep(time_to_sleep)


keep_running = True
time_to_sleep = 0.5
counter = 0

while keep_running:
    if counter == 0:
        to_the_right(True)
    else:
        to_the_right(False)

    right_to_the_bottom()
    to_the_left()
    left_to_the_bottom()

    counter += 1


