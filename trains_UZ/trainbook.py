from tkinter import *

from trains import Trains
from cities_train import Cities
from about_us_UZ import AboutUs

import datetime
import sqlite3

date = datetime.datetime.now().date()

con = sqlite3.connect('train_model.db')
cur = con.cursor()
print(con)

persons = cur.execute("select * from 'train'").fetchall()
print(persons)


class Application(object):
    def trains(self):
        cities = Trains()

    def cities(self):
        cities = Cities()

    def about_us(self):
        cities = AboutUs()

    def __init__(self, master):
        self.master = master

        self.top = Frame(master, height=175, bg='blue')
        self.top.pack(fill=X)
        self.logo = PhotoImage(file='img/uz_sign_for_program.png')
        self.lbl_logo = Label(self.top, image=self.logo)
        self.lbl_logo.place(x=150, y=75)
        self.lbl_date = Label(self.top, text='Today`s date: ' + str(date), font='Verdana 15 bold', bg='blue', fg='white')
        self.lbl_date.place(x=840, y=140)

        self.canvas = Canvas(master, width=1400, height=8)
        self.canvas.pack()
        self.canvas.create_line(0,0,1200,10, width=855, fill='red')

        self.bottom = Frame(master, height=600, bg='navy')
        self.bottom.pack(fill=X)

        self.button1 = Button(self.bottom, text='Trains', relief=RAISED, bg='white', fg='navy', font='Arial 15 bold', command=self.trains)
        self.button1.place(x=600, y=100)
        self.button2 = Button(self.bottom, text='Cities', relief=RAISED, bg='white', fg='navy', font='Arial 15 bold', command=self.cities)
        self.button2.place(x=600, y=150)
        self.button3 = Button(self.bottom, text='About us', relief=RIDGE, bg='white', fg='navy', font='Arial 15 bold', command=self.about_us)
        self.button3.place(x=600, y=200)


def main():
    root = Tk()
    app = Application(root)
    root.title('Booking UZ')
    root.geometry('1150x750+350+200')
    root.resizable(False, False)
    root.mainloop()


if __name__ == '__main__':
    main()
