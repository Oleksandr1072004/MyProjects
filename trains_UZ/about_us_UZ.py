from tkinter import *


class AboutUs(Toplevel):

    def __init__(self):
        Toplevel.__init__(self)

        self.geometry("1150x750+350+200")
        self.title("About us UZ")
        self.resizable(False, False)

        self.top = Frame(self, height=175, bg='blue')
        self.top.pack(fill=X)
        self.logo = PhotoImage(file='img/uz_sign_for_program.png')
        self.map = PhotoImage(file='img/Uz_map_big.png')
        self.lbl_logo = Label(self.top, image=self.logo)
        self.lbl_logo.place(x=150, y=75)

        self.canvas = Canvas(self, width=1400, height=8)
        self.canvas.pack()
        self.canvas.create_line(0, 0, 1200, 10, width=855, fill='red')

        self.bottom = Frame(self, height=600, bg='navy')
        self.bottom.pack(fill=X)

        self.text = Label(self.bottom, text="This page is about us."
                                         "\nThis app made by Alexander Grinenko for example of my power!\n"
                                         "Email: oleksandryrinenko@gmail.com",
                          font='arial 14 bold', bg="#34baeb", fg='white'

                          )

        self.text.place(x=300, y=50)
