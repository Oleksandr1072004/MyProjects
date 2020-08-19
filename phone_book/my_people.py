from tkinter import *
from tkinter import messagebox

import sqlite3

from phone_book import add_person, update_person, display_person

con = sqlite3.connect('phonebook.db')
cur = con.cursor()


class MyPeople(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)

        self.geometry("650x650")
        self.title("My People")
        self.resizable(False, False)

        # frames
        self.top = Frame(self, height=150, bg='white')
        self.top.pack(fill=X)

        self.bottom = Frame(self, height=500, bg='#ebb134')
        self.bottom.pack(fill=X)

        # top frame design
        self.top_image = PhotoImage(file='images/people.png')
        self.top_image_label = Label(self.top, image=self.top_image, bg='white')
        self.top_image_label.place(x=130, y=25)

        self.heading = Label(self.top, text='My People', font='arial 15 bold', bg='white', fg='#ebb434')
        self.heading.place(x=270, y=50)

        self.scroll = Scrollbar(self.bottom, orient=VERTICAL)

        self.listBox = Listbox(self.bottom, width=60, height=31)
        self.listBox.config(yscrollcommand=self.scroll.set)
        self.listBox.grid(row=0, column=0, padx=(40, 0))

        self.scroll.config(command=self.listBox.yview)
        self.scroll.grid(row=0, column=1, sticky=N + S)

        persons = cur.execute("select * from 'addressbook'").fetchall()
        print(persons)

        count = 0
        for person in persons:
            self.listBox.insert(count, str(person[0]) + ". " + person[1] + " " + person[2])
            count += 1

        # Buttons

        self.btn_add = Button(self.bottom, text="Add", width=12, font='Sans 12 bold', command=self.add_new_person)
        self.btn_add.grid(row=0, column=2, padx=40, pady=20, sticky=N)

        self.btn_display = Button(self.bottom, text="Update", width=12, font='Sans 12 bold', command=self.update_person)
        self.btn_display.grid(row=0, column=2, padx=40, pady=70, sticky=N)

        self.btn_update = Button(self.bottom, text="Display", width=12, font='Sans 12 bold', command=self.display_person)
        self.btn_update.grid(row=0, column=2, padx=40, pady=120, sticky=N)

        self.btn_delete = Button(self.bottom, text="Delete", width=12, font='Sans 12 bold', command=self.delete_person)
        self.btn_delete.grid(row=0, column=2, padx=40, pady=170, sticky=N)


    def add_new_person(self):
        add = add_person.AddPerson()
        self.destroy()

    def update_person(self):
        selected_item = self.listBox.curselection()
        print(selected_item)
        person = self.listBox.get(selected_item)
        person_id = person.split(".")[0]
        print(person)
        print(person_id)
        print(person[0])

        update = update_person.UpdatePerson(person_id)

    def display_person(self):
        selected_item = self.listBox.curselection()
        print(selected_item)
        person = self.listBox.get(selected_item)
        person_id = person.split(".")[0]
        display = display_person.DisplayPerson(person_id)

    def delete_person(self):
        selected_item = self.listBox.curselection()
        print(selected_item)
        person = self.listBox.get(selected_item)
        person_id = person.split(".")[0]
        query = "select * from addressbook where person_id = '{}'".format(person_id)
        result = cur.execute(query).fetchone()
        person_name = result[1]
        person_surname = result[2]

        query = "delete from addressbook where person_id = '{}'".format(person_id)
        answer = messagebox.askquestion("Warning", "Are you sure wanna delete " + person_name + " " + person_surname
                                        + "?")
        if answer == "yes":
            try:
                cur.execute(query)
                con.commit()
                messagebox.showinfo("Success", person_name + " " + person_surname + " deleted!")
            except EXCEPTION as e:
                messagebox.showinfo("Info", str(e))
