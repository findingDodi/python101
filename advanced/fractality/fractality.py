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


def move_and_turn(path):
    for i in range(len(path)):
        current_move = path[i]
        if current_move == "F":
            turtle.forward(25)
        elif current_move == "-":
            turtle.left(60)
        elif current_move == "+":
            turtle.right(60)


initiator = "F--F--F"
generator = "F+F--F+F"
turtle.shape("turtle")

for i in range(2):
    initiator = convert(initiator, generator)

move_and_turn(initiator)
turtle.done()
