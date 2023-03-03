import turtle

turtle.color("brown", "green")
turtle.shape("blank")
turtle.speed(2)


def dodos_stern():
    for i in range(5):
        turtle.left(36)
        turtle.forward(50)
        turtle.right(108)
        turtle.forward(50)


def bisons_stern():
    for i in range(5):
        turtle.left(72)
        turtle.forward(50)
        turtle.right(144)
        turtle.forward(50)


def totally_not_dodos_stern():
    turtle.left(45)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(50)

    turtle.left(135)
    turtle.forward(50)
    turtle.right(45)
    turtle.forward(50)

    turtle.left(135)
    turtle.forward(50)
    turtle.right(65)
    turtle.forward(50)

    turtle.left(135)
    turtle.forward(50)
    turtle.right(70)
    turtle.forward(50)

    turtle.left(135)
    turtle.forward(50)
    turtle.right(45)
    turtle.forward(50)

dodos_stern()
bisons_stern()
totally_not_dodos_stern()

turtle.done()
