import tkinter as tk


class Okay(tk.Tk):

    def __init__(self):
        super().__init__()
        self.click_count = 0
        self.geometry("400x100")

        self.button_okay = tk.Button(text="Okay", command=self.okay_button_clicked)
        self.button_okay.pack()

    def okay_button_clicked(self):
        self.click_count += 1
        print(self.click_count)


if __name__ == "__main__":
    not_okay = Okay()
    not_okay.mainloop()
