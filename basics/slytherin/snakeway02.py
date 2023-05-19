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

WIDTH_HORIZONTAL = 10
STEPS_HORIZONTAL = WIDTH_HORIZONTAL - 1
STEPS_VERTICAL = 2


def do_sleep(sleepy_time):
    try:
        time.sleep(sleepy_time)
    except KeyboardInterrupt:
        return False

    return True


def to_the_right(is_start):
    output = ""
    for i in range(WIDTH_HORIZONTAL):
        if i == 0:
            if is_start:
                output = START
            else:
                output = LEFT_RIGHT

        if 0 < i < STEPS_HORIZONTAL:
            output = HORIZONTAL

        if i == STEPS_HORIZONTAL:
            output = RIGHT_DOWN + "\n"

        print(output, end="")
        do_sleep(time_to_sleep)


def right_to_the_bottom():
    for i in range(STEPS_VERTICAL):
        print(SPACE * STEPS_HORIZONTAL + VERTICAL)
        do_sleep(time_to_sleep)


def to_the_left():
    for i in range(STEPS_HORIZONTAL, 0, -1):
        if i == STEPS_HORIZONTAL:
            print(SPACE * STEPS_HORIZONTAL + RIGHT_LEFT, end="")

        if 0 < i < STEPS_HORIZONTAL:
            spaces = SPACE * (i - 1)
            horizontals = HORIZONTAL * (WIDTH_HORIZONTAL - i)
            print(spaces + horizontals + RIGHT_LEFT, end="")

        do_sleep(time_to_sleep)
        print("\33[1D\r", end="", flush=True)

    print(LEFT_DOWN + HORIZONTAL * (STEPS_HORIZONTAL - 1) + RIGHT_LEFT)
    do_sleep(time_to_sleep)


def left_to_the_bottom():
    for i in range(STEPS_VERTICAL):
        print(VERTICAL + SPACE * STEPS_HORIZONTAL)
        do_sleep(time_to_sleep)


keep_running = True
time_to_sleep = 0.5
counter = 0

while keep_running:
    is_first_round = counter == 0
    to_the_right(is_first_round)
    right_to_the_bottom()
    to_the_left()
    left_to_the_bottom()

    counter += 1


