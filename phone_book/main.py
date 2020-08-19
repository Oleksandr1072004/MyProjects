from tkinter import *

import datetime

from phone_book import my_people, add_person, about_us

date = datetime.datetime.now().date()
date = str(date)


class Application(object):
    def __init__(self, master):
        self.master = master


        # frames
        self.top = Frame(master, height=150, bg='white')
        self.top.pack(fill=X)

        self.bottom = Frame(master, height=500, bg='#34baeb')
        self.bottom.pack(fill=X)

        # top frame design
        self.top_image = PhotoImage(file='images/phone_book.png')
        self.top_image_label = Label(self.top, image=self.top_image, bg='white')
        self.top_image_label.place(x=130, y=25)

        self.heading = Label(self.top, text='My Phonebook App', font='arial 15 bold', bg='white', fg='#ebb434')
        self.heading.place(x=230, y=50)

        self.date_label = Label(self.top, text="Today's date: " + date, font='arial 12 bold', bg='white', fg="#ebb434")
        self.date_label.place(x=450, y=110)

        # btn1 - view people
        self.viewButton = Button(self.bottom, text=' My People  ', font='arial 12 bold', fg='#42bcf5', bg='white',
                                 command=self.view_people)
        self.viewButton.place(x=250, y=70)

        # btn2 - add person
        self.addButton = Button(self.bottom, text='Add Person', font='arial 12 bold', fg='#42bcf5', bg='white',
                                command=self.add_new_person)
        self.addButton.place(x=250, y=130)

        # btn3 - about us
        self.aboutButton = Button(self.bottom, text='  About us   ', font='arial 12 bold', fg='#42bcf5', bg='white',
                                  command=self.about_uss)
        self.aboutButton.place(x=250, y=190)

    def view_people(self):
        people = my_people.MyPeople()

    def add_new_person(self):
        add = add_person.AddPerson()

    def about_uss(self):
        about = about_us.AboutUs()


def main():
    root = Tk()
    app = Application(root)
    root.title("PhoneBook App")
    root.geometry("650x550")
    root.resizable(False, False)
    root.mainloop()


if __name__ == '__main__':
    main()
