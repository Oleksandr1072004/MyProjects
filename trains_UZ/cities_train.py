from tkinter import *
from tkinter import ttk

from Full_train_system_Chernivtsi import Train

import sqlite3


class Cities(Toplevel):
    def back_to_f1(self):
        self.f1.tkraise()

    def buy_ticket(self):
        ticket = Train()
        # Train().cbodestination

    def get_city(self, city):
        self.f2.tkraise()
        chernivtsi_trains = ['702D Chernivtsi - Lviv','6472-6471 Kolomya - Vadul-Siret', '150L Chernivtsi - Poltava',
                             '136L Chernivtsi - Odessa', '6472-6471 Kolomya - Vadul-Siret', '136L Chernivtsi - Bilgorod-Dnistrovsky',
                             '008O Chernivtsi - Kyiv']
        self.listbox_city = Listbox(self.f2, width=70, height=26, font='Arial 12 bold')
        self.listbox_city.place(x=25, y=15)
        self.listbox_city.delete(0,END)
        if 'Chernivtsi' in city:
            for train_ce in chernivtsi_trains:
                self.listbox_city.insert(0, train_ce)
        self.button_buy = Button(self.f2, text='Buy ticket', font='Tahoma 15 bold', relief=RAISED, fg='navy',bg='white', command=self.buy_ticket)
        self.button_buy.place(x=800, y=350)

        self.button_back = Button(self.f2, text='<= Back', font='Verdana 15 bold', relief=RIDGE, fg='blue',bg='white', command=self.back_to_f1)
        self.button_back.place(x=800, y=400)

    def __init__(self):
        Toplevel.__init__(self)
        self.cities = ['Kyiv','Chernivtsi','Ivano-Frankivsk','Lviv','Poltava','Kharkiv','Uzhgorod','Odessa','Dnipro',
                       'Ternopil','Vinnitsya','Mariupol','Mykolaiv','Khmelnytskyi','Kirovograd','Kherson','Sumy','Rivne','Cherkasy','Chernihiv']
        self.geometry("1150x750+350+200")
        self.title("Cities")
        self.resizable(False, False)

        self.top = Frame(self, height=175, bg='blue')
        self.top.pack(fill=X)
        self.logo = PhotoImage(file='img/uz_sign_for_program.png')
        self.map = PhotoImage(file='img/Uz_map_big.png')
        self.lbl_logo = Label(self.top, image=self.logo)
        self.lbl_logo.place(x=150, y=75)

        self.canvas = Canvas(self, width=1400, height=8)
        self.canvas.pack()
        self.canvas.create_line(0,0,1200,10, width=855, fill='red')

        self.bottom = Frame(self, height=600, bg='navy')
        self.bottom.pack(fill=X)
        self.f1 = Frame(self.bottom)
        self.f2 = Frame(self.bottom)
        for frame in (self.f1,self.f2):
            frame.place(relx=0.01, rely=0.01, relwidth=0.985, relheight=0.98)
        self.f1.tkraise()
        self.lbl_map = Label(self.f1, image=self.map)
        self.lbl_map.place(x=10, y=50)
        self.enter_city = Label(self.f1, text='Enter a city to find trains', font='Arial 15 bold')
        self.enter_city.place(x=700, y=100)
        self.combobox_list = ttk.Combobox(self.f1, values=self.cities)
        self.combobox_list.place(x=700, y=150)
        self.button = Button(self.f1, text='OK', relief=RIDGE, bg='white', fg='navy', font='Verdana 15 bold', command=lambda: self.get_city(self.combobox_list.get()))
        self.button.place(x=700, y=200)
