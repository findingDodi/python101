import turtle

# wiederhole x-mal:
# F -- F -- F
# F -> F + F -- F + F
# F = forward, - = left(60), + = right(60)


def convert(_initiator, _generator):
    initiator_array = list(_initiator)

    for i in range(len(initiator_array)):
        if initiator_array[i] == "F":
            initiator_array[i] = _generator

    return "".join(initiator_array)


def move_and_turn(path, distance):
    for current_move in path:
        if current_move == "F":
            turtle.forward(distance)
        elif current_move == "-":
            turtle.left(60)
        elif current_move == "+":
            turtle.right(60)


initiator = "F--F--F"
generator = "F+F--F+F"
loop_amount = 4
distance = 20 / loop_amount

for i in range(loop_amount):
    initiator = convert(initiator, generator)

turtle.shape("turtle")
turtle.speed(0.1)
move_and_turn(initiator, distance)
turtle.done()
