import turtle

#turtle.bgcolor("black")


def turtle_square(my_turtle):
    my_turtle.shape("turtle")
    my_turtle.color("blue", "red")
    my_turtle.speed(1)
    my_turtle.begin_fill()
    for i in range(4):
        my_turtle.forward(150)
        my_turtle.left(90)
    my_turtle.color("red", "blue")
    my_turtle.end_fill()
    my_turtle.done()


def turtle_circle():
    turtle.shape("turtle")
    turtle.color("magenta", "cyan")
    turtle.speed(1)
    turtle.begin_fill()
    turtle.circle(100)
    turtle.left(10)
    turtle.color("cyan", "magenta")
    turtle.end_fill()
    turtle.done()


def turtle_star():
    turtle.shape("turtle")
    turtle.color("red", "green")
    turtle.speed(1)
    turtle_distance = 100
    turtle_acute_angle = 72
    turtle_obtuse_angle = 144
    turtle.begin_fill()
    for i in range(5):
        turtle.forward(turtle_distance)
        turtle.left(turtle_acute_angle)
        turtle.forward(turtle_distance)
        turtle.right(turtle_obtuse_angle)
    turtle.color("yellow", "red")
    turtle.end_fill()
    turtle.done()


def turtle_spirograph():
    turtle.shape("turtle")
    turtle.color("yellow", "green")
    turtle.speed(1)
    for i in range(6):
        for color in ("red", "magenta", "violet", "blue", "cyan", "green", "white"):
            turtle.color(color)
            turtle.circle(100)
            turtle.left(10)
    turtle.done()


def turtle_heart():
    turtle.shape("turtle")
    turtle.color("red", "magenta")
    turtle.fillcolor("magenta")
    turtle.speed(1)
    turtle.begin_fill()
    turtle.left(52)
    turtle.forward(120)
    turtle.circle(45, 200)
    turtle.left(221)
    turtle.circle(45, 200)
    turtle.forward(120)
    turtle.color("black", "magenta")
    turtle.end_fill()
    turtle.done()


def draw_turtle_shape(users_choice):
    turtle.clear()

    if users_choice == "a":
        turtle_square()

    if users_choice == "b":
        turtle_circle()

    if users_choice == "c":
        turtle_star()

    if users_choice == "d":
        turtle_spirograph()

    if users_choice == "e":
        turtle_heart()





