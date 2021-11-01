from tkinter import *
import random, string


def print_rb():
    if var.get() == 0:
        # label_n['text'] = f'Len: {len("Nums")}'
        n_l = []
        entry.delete(0, END)
        for i in range(int(entry1.get())):
            n_l.append(random.randint(0,9))
        entry.insert(0, ''.join(str(x) for x in n_l))
    elif var.get() == 1:
        # label_n['text'] = f'Len: {len("Alfas")}'
        a_l = []
        entry.delete(0,END)
        for i in range(int(entry1.get())):
            a_l.append(random.choice(string.ascii_letters))
        entry.insert(0, ''.join(str(x) for x in a_l))
    elif var.get() == 2:
        # label_n['text'] = f'Len: {len("Alnums")}'
        aln_l = []
        entry.delete(0, END)
        for i in range(int(entry1.get()) * 2):
            aln_l.append(random.randint(0,9))
            aln_l.append(random.choice(string.ascii_letters))
        entry.insert(0, ''.join(str(random.choice(aln_l)) for i in range(int(entry1.get()))))
    elif var.get() == 3:
        # label_n['text'] = f'Len: {len("Alnums_symbols")}'
        aln_s_l = []
        entry.delete(0, END)
        symbols = ['-','_','=','+','-',')','(','*','&','^','%','$','#','@','!','`','~','|','/','\\','<','>']
        for i in range(int(entry1.get()) * 3):
            aln_s_l.append(random.randint(0,9))
            aln_s_l.append(random.choice(string.ascii_letters))
            aln_s_l.append(random.choice(symbols))
        entry.insert(0, ''.join(str(random.choice(aln_s_l)) for i in range(int(entry1.get()))))


root = Tk()
root.geometry('500x350')

entry = Entry(root, font='Arial 12 bold', width=25)
entry.place(relx=0.25, rely=0.05)

var = IntVar()
var.set(0)

radiobutton_n = Radiobutton(root, text='Nums', variable=var, value=0)
radiobutton_n.place(relx=0.1, rely=0.2)
radiobutton_alf = Radiobutton(root, text='Alfas', variable=var, value=1)
radiobutton_alf.place(relx=0.3, rely=0.2)
radiobutton_aln = Radiobutton(root, text='Alnums', variable=var, value=2)
radiobutton_aln.place(relx=0.5, rely=0.2)
radiobutton_aln_s = Radiobutton(root, text='Alnums_symbols', variable=var, value=3)
radiobutton_aln_s.place(relx=0.7, rely=0.2)

label_n = Label(root, text='Len: ', font='Arial 12 bold')
label_n.place(relx=0.1, rely=0.35)

entry1 = Entry(root, font='Arial 12 bold', width=25)
entry1.place(relx=0.35, rely=0.35)

button = Button(root, text='Button', width=15, font='Arial 12 bold', command=print_rb)
button.place(relx=0.4, rely=0.55)
root.mainloop()
