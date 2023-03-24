import turtle
import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")


def square():
    for i in range(4):
        the_turtle.forward(150)
        the_turtle.left(90)


app = customtkinter.CTk()
app.title("Test")

canvas = customtkinter.CTkCanvas(master=app, width=1200, height=600)
canvas.grid(row=0, column=1)

the_turtle = turtle.RawTurtle(canvas)
the_turtle.screen.bgcolor("black")
the_turtle.pencolor("red")
#the_turtle.penup()
#the_turtle.pendown()

the_button = customtkinter.CTkButton(master=app, text="Square", command=square)
the_button.grid(row=0, column=0)

app.mainloop()
