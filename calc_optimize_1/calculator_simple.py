from tkinter import *


class Calculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Calculator")
        self.master.resizable(False, False)

        self.frame_entry = Frame(self.master, height=50, bg='silver')
        self.frame_entry.pack(fill=X)
        self.entry = Entry(self.frame_entry, font='Arial 16 bold')
        self.entry.pack(fill=X)
        self.frame_buttons = Frame(self.master, height=500, bg='gray')
        self.frame_buttons.pack(fill=X)
        self.frame_nums_buttons = Frame(self.frame_buttons, height=500, width=350, bg='gray')
        self.frame_nums_buttons.pack(side=LEFT)
        self.button_1 = Button(self.frame_nums_buttons, text='1',
                                font='Arial 20 bold', command=lambda: self.add_num(1))
        self.button_1.grid(row=0, column=0)
        self.button_2 = Button(self.frame_nums_buttons, text='2',
                                font='Arial 20 bold', command=lambda: self.add_num(2))
        self.button_2.grid(row=0, column=1)
        self.button_3 = Button(self.frame_nums_buttons, text='3',
                                font='Arial 20 bold', command=lambda: self.add_num(3))
        self.button_3.grid(row=0, column=2)
        self.button_4 = Button(self.frame_nums_buttons, text='4',
                                font='Arial 20 bold', command=lambda: self.add_num(4))
        self.button_4.grid(row=0, column=3)
        self.button_5 = Button(self.frame_nums_buttons, text='5',
                               font='Arial 20 bold', command=lambda: self.add_num(5))
        self.button_5.grid(row=1, column=0)
        self.button_6 = Button(self.frame_nums_buttons, text='6',
                               font='Arial 20 bold', command=lambda: self.add_num(6))
        self.button_6.grid(row=1, column=1)
        self.button_7 = Button(self.frame_nums_buttons, text='7',
                               font='Arial 20 bold', command=lambda: self.add_num(7))
        self.button_7.grid(row=1, column=2)
        self.button_8 = Button(self.frame_nums_buttons, text='8',
                               font='Arial 20 bold', command=lambda: self.add_num(8))
        self.button_8.grid(row=1, column=3)
        self.button_9 = Button(self.frame_nums_buttons, text='9',
                               font='Arial 20 bold', command=lambda: self.add_num(9))
        self.button_9.grid(row=2, column=0)
        self.button_start = Button(self.frame_nums_buttons, text='(',
                               font='Arial 20 bold', command=lambda: self.add_operation('('))
        self.button_start.grid(row=2, column=1)
        self.button_zero = Button(self.frame_nums_buttons, text='0',
                               font='Arial 20 bold', command=lambda: self.add_num(0))
        self.button_zero.grid(row=2, column=2)
        self.button_end = Button(self.frame_nums_buttons, text=')',
                               font='Arial 20 bold', command=lambda: self.add_operation(')'))
        self.button_end.grid(row=2, column=3)
        self.frame_operations_buttons = Frame(self.frame_buttons, height=500,
                                        width=150, bg='gray')
        self.frame_operations_buttons.pack(side=LEFT, padx=5)
        self.button_c = Button(self.frame_operations_buttons, text='C',
                                font='Arial 20 bold', command=lambda: self.clear_entry())
        self.button_c.grid(row=0, column=0)
        self.button_eval = Button(self.frame_operations_buttons, text='=',
                                font='Arial 20 bold', command=lambda: self.equal_operation())
        self.button_eval.grid(row=0, column=1)
        self.button_plus = Button(self.frame_operations_buttons, text='+',
                                font='Arial 20 bold', command=lambda: self.add_operation('+'))
        self.button_plus.grid(row=1, column=0)
        self.button_minus = Button(self.frame_operations_buttons, text='-',
                               font='Arial 20 bold', command=lambda: self.add_operation('-'))
        self.button_minus.grid(row=1, column=1)
        self.button_multiply = Button(self.frame_operations_buttons, text='*',
                                  font='Arial 20 bold', command=lambda: self.add_operation('*'))
        self.button_multiply.grid(row=2, column=0)
        self.button_divide = Button(self.frame_operations_buttons, text='/',
                                   font='Arial 20 bold', command=lambda: self.add_operation('/'))
        self.button_divide.grid(row=2, column=1)

    def clear_entry(self):
        self.entry.delete(0, END)

    def add_num(self, num):
        self.entry.insert(END, str(num))

    def add_operation(self, symbol):
        self.entry.insert(END, symbol)

    def equal_operation(self):
        res = self.entry.get()
        print(res)
        l = eval(res)
        print(l)
        self.entry.delete(0, END)
        self.entry.insert(END,str(l))


if __name__ == '__main__':
    root = Tk()
    Calculator(root)
    root.mainloop()
