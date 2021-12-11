from tkinter import *
from tkinter import ttk
from tkinter import messagebox

from add_train import AddTrain

import sqlite3

con = sqlite3.connect('train_model.db')
cur = con.cursor()


class Trains(Toplevel):
    def get_info(self, train):
        image_file = ''
        info_text = 'Locomotive: ' + str(train)
        if 'ЧС4' in train or 'ЧС8' in train or 'ДС3' in train:
            info_text = 'Locomotive: ' + str(train) + '\nHome road: South-west railway\nDepot: TЧ-1 Kyiv Passenger\nCategory: Alternating current electric locomotives'
            if 'ЧС4' in train:
                image_file = 'img/chs4_krp.png'
            if 'ЧС8' in train:
                image_file = 'img/chs8_006.png'
            if 'ДС3' in train:
                image_file = 'img/ds3_011.png'
        elif 'ВЛ10' in train or 'ЧС2' in train or 'ЧС2 КРП' in train or 'ЧС7' in train:
            info_text = 'Locomotive: ' + str(train) + '\nHome road: Lviv railway\nDepot: TЧ-1 Lviv-West\nCategory: Direct current electric locomotives'
            if 'ВЛ10' in train:
                image_file = 'img/vl10_1491.png'
            elif 'ЧС2' in train or 'ЧС2 КРП' in train:
                image_file = 'img/chs2_krp.png'
            elif 'ЧС7' in train:
                image_file = 'img/chs7_122.png'
        elif 'ВЛ11M' in train:
            info_text = 'Locomotive: ' + str(train) + '\nHome road: Lviv railway\nDepot: TЧ-9 Mukachevo\nCategory: Direct current electric locomotives'
        elif 'ВЛ11.8' in train:
            info_text = 'Locomotive: ' + str(train) + '\nHome road: South railway\nDepot: TЧ-10 Kharkiv\nCategory: Direct current electric locomotives'
        elif '2ЭЛ4' in train or 'ДЭ1' in train:
            info_text = 'Locomotive: ' + str(train) + '\nHome road: Donetsk railway\nDepot: TЧ-1 Liman\nCategory: Direct current electric locomotives'
        elif 'ВЛ8' in train or 'ВЛ8М' in train:
            info_text = 'Locomotive: ' + str(train) + '\nHome road: Dnieper railway\nDepot: TЧ-8 Melitopol\nCategory: Direct current electric locomotives'
        elif 'ВЛ40У (ЗЭРЗ)' in train or 'ВЛ60К' in train or 'ВЛ60ПК' in train or 'ВЛ80С' in train or '2ЭЛ5' in train or '2ЭС5К' in train:
            info_text = 'Locomotive: ' + str(train) + '\nHome road: Odessa railway\nDepot: TЧ-2 Podolsk\nCategory: Alternating current electric locomotives'
        info = Toplevel()
        info.title('Info')
        info.geometry('1300x1000')
        image = PhotoImage(file=image_file)
        label_image = Label(info, image=image)
        label_image.pack()
        label_info = Label(info, text=info_text, font='Arial 10 bold')
        label_info.pack()
        info.resizable(False, False)
        info.mainloop()

    def add_train(self):
        add_train = AddTrain()

    def __init__(self):
        Toplevel.__init__(self)
        self.electric_trains = ['ЧС2','ЧС2 КРП','ЧС4','ЧС7','ЧС8','ДС3', 'ДЭ1','ВЛ8','ВЛ8М','ВЛ10','ВЛ11.8','ВЛ11М','ВЛ40У (ЛЛРЗ)',
                       'ВЛ40У (ЗЭРЗ)','ВЛ60К','ВЛ60ПК','ВЛ80К','ВЛ80Т','ВЛ80С','ВЛ82М','2ЭЛ4','2ЭЛ5','2ЭС5К']
        self.steam_trains = ['К159','Эр','Л','Су']
        self.diesel_trains = ['2М62', '2М62К', '2М62У', '2ТЭ10М', '2ТЭ10У', '2ТЭ10УТ', '2ТЭ116', 'ТЭП70', 'ТЭ33АС',
                                'АС4400CW', 'М62', 'М62М', 'ТЭМ2', 'ТЭМ2У', 'ТЭМ2УM', 'ТГК2', 'ТГМ4', 'ЧМЭ2', 'ЧМЭ3', 'ЧМЭ3Т',
                              'ЧМЭ3Э', 'ТЭ2', 'ТЭ3', 'ТЭ7', '2ТЭ10Л']
        self.commuter_diesel_trains = ['Д1', 'ДР1А', 'ДПЛ1','ДТЛ1','ДПЛ2','ДТЛ2','ДПКр2','ДПКр3','620М','630М','ДЭЛ02']
        self.commuter_electric_trains = ['ЭР1', 'ЭР2', 'ЭР2Р', 'ЭР2Т', 'ЭР9П', 'ЭР9М', 'ЭР9Е', 'ЭР9Т', 'ЭПЛ2Т', 'ЭПЛ9Т',
                                      'ЭД9М','Hyundai HRCS2','Skoda EJ675','ЭКр1']
        self.passenger_wagons = ['Плацкарт', 'Купе', 'Люкс', 'Плацкарт (КВЗ)', 'Купе (КВЗ)', 'Люкс (КВЗ)', 'Спальный вагон РИЦ',
                       'Штабной вагон', 'Вагон-ресторан', 'Штабной вагон (КВЗ)', 'Вагон-ресторан (КВЗ)']
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
        self.enter_city = Label(self.f1, text='Trains', font='Arial 15 bold')
        self.enter_city.place(x=700, y=100)
        self.combobox_list = ttk.Combobox(self.f1, values=self.electric_trains)
        self.combobox_list.place(x=700, y=150)
        train_select = self.combobox_list.get()
        print(train_select)
        self.button = Button(self.f1, text='Find the information', relief=RIDGE, bg='white', fg='navy', font='Verdana 15 bold', command=lambda: self.get_info(self.combobox_list.get()))
        self.button.place(x=700, y=200)
        self.button_add = Button(self.f1, text='Add train', font='Tahoma 15 bold', relief=GROOVE, bg='white', fg='navy', command=self.add_train)
        self.button_add.place(x=700, y=250)
