import tkinter as tk
from tkinter import messagebox
import datetime


class Okay(tk.Tk):

    def __init__(self):
        super().__init__()
        self.click_count = 0
        self.geometry("400x200")
        self.date_clicked = False

        self.button_okay = tk.Button(text="Okay", command=self.okay_button_clicked)
        self.button_okay.pack()

        self.label_count = tk.Label(text=str(self.click_count))
        self.label_count.pack()

        self.button_date = tk.Button(text="Show Date", command=self.date_button_clicked)
        self.button_date.pack()

        self.label_date = tk.Label(text="nothing to see yet")
        self.label_date.pack()

    def okay_button_clicked(self):
        self.click_count += 1
        self.label_count.config(text=str(self.click_count))
        print(self.click_count)

    def date_button_clicked(self):
        # messagebox.showinfo(title="Today's date is: ", message=str(datetime.date.today()))

        if self.date_clicked:
            self.label_date.config(text="nothing to see yet")
            self.date_clicked = False
        elif not self.date_clicked:
            self.label_date.config(text=str(datetime.date.today()))
            self.date_clicked = True


if __name__ == "__main__":
    not_okay = Okay()
    not_okay.mainloop()
