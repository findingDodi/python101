import turtle

turtle.color("brown", "green")
turtle.shape("turtle")
turtle.speed(2)
for i in range(4):
    turtle.forward(100)
    turtle.left(90)

turtle.goto(20, 20)
turtle.penup()
turtle.goto(40, 40)
turtle.pendown()
turtle.goto(100, 100)

turtle.done()
