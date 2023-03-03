import turtle

turtle.color("brown", "green")
turtle.shape("turtle")
turtle.speed(2)

distance = 10
for i in range(4):
    for j in range(4):
        turtle.forward(distance)
        turtle.pendown()
        turtle.forward(distance)
        turtle.penup()

    turtle.left(90)


turtle.done()
