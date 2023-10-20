import turtle

# wiederhole x-mal:
# F -- F -- F
# F -> F + F -- F + F
# F = forward, - = left(60), + = right(60)


def convert(_initiator, _generator):
    return _initiator.replace("F", _generator)


def move_and_turn(_path, _distance):
    for current_move in _path:
        if current_move == "F":
            turtle.forward(_distance)
        elif current_move == "-":
            turtle.left(60)
        elif current_move == "+":
            turtle.right(60)


initiator = "F--F--F"
generator = "F+F--F+F"
loop_amount = 4
turtle.shape("turtle")
turtle.speed(0.1)

for i in range(loop_amount):
    distance = 20 / (i + 1)
    initiator = convert(initiator, generator)
    move_and_turn(initiator, distance)
    # turtle.setheading(0)

turtle.done()
