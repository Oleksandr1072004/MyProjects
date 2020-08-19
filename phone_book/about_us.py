from tkinter import *


class AboutUs(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)

        self.geometry("600x400")
        self.title("About us")
        self.resizable(False, False)

        self.top = Frame(self, height=400, width=600, bg='#ffa550')
        self.top.pack(fill=BOTH)

        self.label_main = Label(self.top, text="opridolob@mail.ru", font="arial 15 bold", fg='#42bcf5')
        self.label_main.place(x=230, y=50)