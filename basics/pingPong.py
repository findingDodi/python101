import time

START = "["
END = "]"
BALL = "O"
SEPARATOR = " "
LENGTH = 15
SLEEPY_TIME = 0.5


def get_output_string(ball_position):
    output_string = START
    for i in range(LENGTH):
        if i == ball_position:
            output_string += BALL
        else:
            output_string += SEPARATOR
    output_string += END
    return output_string


counter = 0
while counter < LENGTH:

    for i in range(LENGTH - 1):
        print(get_output_string(i))
        time.sleep(SLEEPY_TIME)

    for i in range((LENGTH - 1), 0, -1):
        print(get_output_string(i))
        time.sleep(SLEEPY_TIME)

    counter += 1
