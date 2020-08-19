from tkinter import *
from tkinter import messagebox

import sqlite3

con = sqlite3.connect("phonebook.db")
cur = con.cursor()


class AddPerson(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)

        self.geometry("400x650")
        self.title("Add person")
        self.resizable(False, False)

        # frames
        self.top = Frame(self, height=150, bg='white')
        self.top.pack(fill=X)

        self.bottom = Frame(self, height=500, bg='#ebb134')
        self.bottom.pack(fill=X)

        # top frame design
        self.top_image = PhotoImage(file='images/people.png')
        self.top_image_label = Label(self.top, image=self.top_image, bg='white')
        self.top_image_label.place(x=90, y=25)

        self.heading = Label(self.top, text='Add new person', font='arial 15 bold', bg='white', fg='#ebb434')
        self.heading.place(x=180, y=50)

        # name
        self.lbl_name = Label(self.bottom, text="Name", font="arial 15 bold", bg="#fcc324")
        self.lbl_name.place(x=40, y=40)

        self.entry_name = Entry(self.bottom, width=30, bd=4)
        self.entry_name.insert(0, "enter Name")
        self.entry_name.place(x=150, y=40)

        # surname
        self.lbl_surname = Label(self.bottom, text="Surname", font="arial 15 bold", bg="#fcc324")
        self.lbl_surname.place(x=40, y=80)

        self.entry_surname = Entry(self.bottom, width=30, bd=4)
        self.entry_surname.insert(0, "enter Surname")
        self.entry_surname.place(x=150, y=80)

        # email
        self.lbl_email = Label(self.bottom, text="Email", font="arial 15 bold", bg="#fcc324")
        self.lbl_email.place(x=40, y=120)

        self.entry_email = Entry(self.bottom, width=30, bd=4)
        self.entry_email.insert(0, "enter Email")
        self.entry_email.place(x=150, y=120)

        # phone number
        self.lbl_phone = Label(self.bottom, text="Phone", font="arial 15 bold", bg="#fcc324")
        self.lbl_phone.place(x=40, y=160)

        self.entry_phone = Entry(self.bottom, width=30, bd=4)
        self.entry_phone.insert(0, "enter Phone number")
        self.entry_phone.place(x=150, y=160)

        # address
        self.lbl_address = Label(self.bottom, text="Address", font="arial 15 bold", bg="#fcc324")
        self.lbl_address.place(x=40, y=200)

        self.entry_address = Text(self.bottom, width=23, height=10)
        self.entry_address.place(x=150, y=200)

        # button
        self.btn = Button(self.bottom, width=12, text="Add person", command=self.add_new_person)
        self.btn.place(x=270, y=420)

    def add_new_person(self):
        name = self.entry_name.get()
        surname = self.entry_surname.get()
        email = self.entry_email.get()
        phone = self.entry_phone.get()
        address = self.entry_address.get(1.0, 'end-1c')

        if name and surname and email and phone and address != "":
            try:
                query = "insert into 'addressbook' (person_name, person_surname, person_email, person_phone, person_address) values (?,?,?,?,?)"
                cur.execute(query, (name, surname, email, phone, address))
                con.commit()
                messagebox.showinfo("Success", "Contact add")

            except EXCEPTION as e:
                messagebox.showerror("Error", str(e))
        else:
            messagebox.showerror("Error", "Fill all the fields!", icon='warning')