import turtle

import customtkinter
import turtle_00 as my_turtle

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("CustomTkinter Turtle")
        self.geometry(f"{1100}x{580}")

        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure((1, 2), weight=1)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # sidebar
        self.sidebar_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=3, sticky="nsew")
        #self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Drawing Turtle")
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        self.canvas = customtkinter.CTkCanvas(self, width=900, height=580)
        self.canvas.grid(row=0, column=1, rowspan=3)
        #self.canvas.pack()

        self.screen = turtle.TurtleScreen(self.canvas)
        #self.screen.bgcolor("black")

        self.draw = turtle.RawTurtle(self.screen, shape="turtle")
        self.draw.screen.bgcolor("black")
        self.draw.pencolor("red")
        self.draw.pendown()

        self.screen.listen()

        self.shape_label = customtkinter.CTkLabel(self.sidebar_frame, text="Shape:", anchor="w")
        self.shape_label.grid(row=1, column=0, padx=20, pady=(10, 0))
        #self.shape_optionmenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["a", "b", "c", "d", "e"], command=self.draw_turtle_shape)
        #self.shape_optionmenu.grid(row=2, column=0, padx=20, pady=(10, 10))
        self.button = customtkinter.CTkButton(self.sidebar_frame, text="Square", command=self.draw_turtle_shape)
        self.button.grid(row=2, column=0, padx=20, pady=10)

    def draw_turtle_shape(self):
        self.draw.forward(150)
        self.draw.left(90)


if __name__ == '__main__':
    app = App()
    app.mainloop()
