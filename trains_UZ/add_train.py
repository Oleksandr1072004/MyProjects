from tkinter import *
from tkinter import messagebox

# from trains import Trains

import sqlite3

con = sqlite3.connect('train_model.db')
cur = con.cursor()


class AddTrain(Toplevel):

    def add_train(self):
        home_road = self.entry_home_road.get()
        depot = self.entry_depot.get()
        model = self.entry_model.get()
        factory = self.entry_factory.get()
        build_in = self.entry_build.get()
        category = self.entry_category.get()

        # trains = Trains()
        self.destroy()

        if home_road and depot and model and factory and build_in and category !=0:
            try:
                query = "insert into 'train' (home_road, depot, model, factory, build, category) values (?,?,?,?,?,?)"
                cur.execute(query, (home_road, depot, model, factory, build_in, category))
                con.commit()
                messagebox.showinfo("Success", "Train add")
            except EXCEPTION as e:
                messagebox.showerror('Error', str(e))
        else:
            messagebox.showerror('Error', 'Fill all the fields!', icon='warning')

    def __init__(self):
        Toplevel.__init__(self)

        self.geometry("1150x750+350+200")
        self.title("Trains UZ")
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

        self.heading = Label(self.top, text='Add new train', font='arial 25 bold', bg='blue', fg='white')
        self.heading.place(x=500, y=100)

        # home road
        self.label_home_road = Label(self.bottom, text='Home road:', font='arial 15 bold', fg='white', bg='blue')
        self.label_home_road.place(x=49, y=40)

        self.entry_home_road = Entry(self.bottom, width=30, bd=4)
        self.entry_home_road.insert(0, 'Enter home road')
        self.entry_home_road.place(x=200, y=40)

        # depot
        self.label_depot = Label(self.bottom, text='Depot:', font='arial 15 bold', fg='white', bg='blue')
        self.label_depot.place(x=49, y=80)

        self.entry_depot = Entry(self.bottom, width=30, bd=4)
        self.entry_depot.insert(0, 'Enter depot')
        self.entry_depot.place(x=200, y=80)

        # model
        self.label_model = Label(self.bottom, text='Model:', font='arial 15 bold', fg='white', bg='blue')
        self.label_model.place(x=49, y=120)

        self.entry_model = Entry(self.bottom, width=30, bd=4)
        self.entry_model.insert(0, 'Enter model of train')
        self.entry_model.place(x=200, y=120)

        # factory
        self.label_factory = Label(self.bottom, text='Factory:', font='arial 15 bold', fg='white', bg='blue')
        self.label_factory.place(x=49, y=160)

        self.entry_factory = Entry(self.bottom, width=30, bd=4)
        self.entry_factory.insert(0, 'Enter factory, where train builded')
        self.entry_factory.place(x=200, y=160)

        # build in
        self.label_build = Label(self.bottom, text='Build:', font='arial 15 bold', fg='white', bg='blue')
        self.label_build.place(x=49, y=200)

        self.entry_build = Entry(self.bottom, width=30, bd=4)
        self.entry_build.insert(0, 'Enter, when train builded')
        self.entry_build.place(x=200, y=200)

        # category
        self.label_category = Label(self.bottom, text='Category:', font='arial 15 bold', fg='white', bg='blue')
        self.label_category.place(x=49, y=240)

        self.entry_category = Entry(self.bottom, width=30, bd=4)
        self.entry_category.insert(0, 'Enter category')
        self.entry_category.place(x=200, y=240)

        # Button

        button = Button(self.bottom, text='Add train', font='arial 15 bold', fg='navy', relief=GROOVE, width=27, height=1, command=self.add_train)
        button.place(x=147, y=350)
