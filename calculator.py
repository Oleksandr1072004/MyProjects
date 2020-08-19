from tkinter import *

root = Tk()
root.title("Calculator")
root.geometry("380x500")


def entry_number(x):
    if entry_box.get() == '0':
        if x == '.':
            entry_box.insert(1, '0.')
        else:
            entry_box.delete(0, END)
            entry_box.insert(0, str(x))
    else:
        length = len(entry_box.get())
        print(length)
        entry_box.insert(length, str(x))


def enter_operator(x):
    if entry_box.get() != "0":
        length = len(entry_box.get())
        all_text = entry_box.get()
        last_char = all_text[-1:]
        if last_char in ['+', '-', '*', '/'] or all_text[-2:] == "**" :
            pass
        else:
            entry_box.insert(length, btn_operator[x]['text'])


def fun_clear():
    entry_box.delete(0, END)
    entry_box.insert(0, '0')


history = []


def func_operator():
    content = entry_box.get()
    result = eval(content)
    entry_box.delete(0, END)
    entry_box.insert(0, result)
    history.append(content + "=" + str(result))
    history.reverse()

    status.configure(text="History: " + " | ".join(history[:3]), font='verdana 10 bold')


def func_delete():
    length = len(entry_box.get())
    entry_box.delete(length - 1, 'end')
    if length == 1:
        entry_box.insert(0, '0')


entry_box = Entry(root, font='verdana 14 bold', width=22, bd=6, justify=RIGHT, bg="#e6e6fa")
entry_box.insert(0, "0")
entry_box.place(x=30, y=10)

btn_numbers = []
for i in range(10):
    btn_numbers.append(Button(width=4, text=str(i), bd=10, command=lambda x=i: entry_number(x)))

btn_text = 1
for i in range(0, 3):
    for j in range(0, 3):
        btn_numbers[btn_text].place(x=30 + j * 90, y=70 + i * 70)
        btn_text += 1

btn_zero = Button(width=30, text='0', bd=10, command=lambda x=0: entry_number(x))
btn_zero.place(x=30, y=280)
btn_dot = Button(width=4, text='.', font='times 15 bold', bd=5, command=lambda x='.': entry_number(x))
btn_dot.place(x=110, y=340)

status = Label(root, text="History: ", relief=SUNKEN, height=3, anchor=W, font='verdana 11 bold')
status.pack(side=BOTTOM, fill=X)

btn_operator = []

for i in range(4):
    btn_operator.append(Button(width=4, font="times 14 bold", bd=5, command=lambda x=i: enter_operator(x)))

btn_operator[0]['text'] = '+'
btn_operator[1]['text'] = '-'
btn_operator[2]['text'] = '*'
btn_operator[3]['text'] = '/'

for i in range(4):
    btn_operator[i].place(x=290, y=70 + i * 70)

btn_clear = Button(width=4, text='C', font='times 15 bold', bd=5, command=fun_clear)
btn_clear.place(x=25, y=340)
btn_equal = Button(width=4, text='=', font='times 15 bold', bd=5, command=func_operator)
btn_equal.place(x=200, y=340)
btn_del = Button(width=4, text='del', font='times 15 bold', bd=5, command=func_delete)
btn_del.place(x=290, y=340)

root.mainloop()
