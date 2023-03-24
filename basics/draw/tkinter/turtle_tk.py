import turtle
import tkinter as tk


def forward():
    t.forward(100)


def back():
    t.back(100)


def left():
    t.left(90)


def square():
    for i in range(4):
        t.forward(150)
        t.left(90)


root = tk.Tk()
canvas = tk.Canvas(master=root, width=500, height=500)
canvas.pack()

t = turtle.RawTurtle(canvas)
t.pencolor("#ff0000")

# Regarding one of the comments
t.penup()
# Regarding one of the comments
t.pendown()

tk.Button(master=root, text="Forward", command=forward).pack()
tk.Button(master=root, text="Back", command=back).pack()
tk.Button(master=root, text="Left", command=left).pack()
tk.Button(master=root, text="Right", command=square).pack()

root.mainloop()
