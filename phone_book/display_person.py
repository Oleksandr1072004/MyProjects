from tkinter import *
from tkinter import messagebox

import sqlite3

con = sqlite3.connect("phonebook.db")
cur = con.cursor()


class DisplayPerson(Toplevel):
    def __init__(self, person_id):
        Toplevel.__init__(self)

        self.geometry("400x650")
        self.title("Display person")
        self.resizable(False, False)

        self.person_id = person_id
        query = "select * from addressbook where person_id = '{}'".format(self.person_id)
        result = cur.execute(query).fetchone()
        self.person_name = result[1]
        self.person_surname = result[2]
        self.person_email = result[3]
        self.person_phone = result[4]
        self.person_address = result[5]

        # frames
        self.top = Frame(self, height=150, bg='white')
        self.top.pack(fill=X)

        self.bottom = Frame(self, height=500, bg='#ebb134')
        self.bottom.pack(fill=X)

        # top frame design
        self.top_image = PhotoImage(file='images/people.png')
        self.top_image_label = Label(self.top, image=self.top_image, bg='white')
        self.top_image_label.place(x=90, y=25)

        self.heading = Label(self.top, text=self.person_name + " " + self.person_surname, font='arial 15 bold',
                             bg='white', fg='#ebb434')
        self.heading.place(x=180, y=50)

        # name
        self.lbl_name = Label(self.bottom, text="Name", font="arial 15 bold", bg="#fcc324")
        self.lbl_name.place(x=40, y=40)

        self.entry_name = Entry(self.bottom, width=30, bd=4)
        self.entry_name.insert(0, self.person_name)
        self.entry_name.config(state='disabled')
        self.entry_name.place(x=150, y=40)

        # surname
        self.lbl_surname = Label(self.bottom, text="Surname", font="arial 15 bold", bg="#fcc324")
        self.lbl_surname.place(x=40, y=80)

        self.entry_surname = Entry(self.bottom, width=30, bd=4)
        self.entry_surname.insert(0, self.person_surname)
        self.entry_surname.config(state='disabled')
        self.entry_surname.place(x=150, y=80)

        # email
        self.lbl_email = Label(self.bottom, text="Email", font="arial 15 bold", bg="#fcc324")
        self.lbl_email.place(x=40, y=120)

        self.entry_email = Entry(self.bottom, width=30, bd=4)
        self.entry_email.insert(0, self.person_email)
        self.entry_email.config(state='disabled')
        self.entry_email.place(x=150, y=120)

        # phone number
        self.lbl_phone = Label(self.bottom, text="Phone", font="arial 15 bold", bg="#fcc324")
        self.lbl_phone.place(x=40, y=160)

        self.entry_phone = Entry(self.bottom, width=30, bd=4)
        self.entry_phone.insert(0, self.person_phone)
        self.entry_phone.config(state='disabled')
        self.entry_phone.place(x=150, y=160)

        # address
        self.lbl_address = Label(self.bottom, text="Address", font="arial 15 bold", bg="#fcc324")
        self.lbl_address.place(x=40, y=200)

        self.entry_address = Text(self.bottom, width=23, height=10)
        self.entry_address.insert(1.0, self.person_email)
        self.entry_address.config(state='disabled')
        self.entry_address.place(x=150, y=200)
