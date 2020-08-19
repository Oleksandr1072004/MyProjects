from tkinter import *
import pickle
bomb = 100  # таймер на 100 секунд
score = 0
best_score = 0
press_return = True  # запуск гри


def start(event):
    global press_return
    global bomb
    global score
    if not press_return:
        pass
    else:
        bomb = 100
        score = 0
        label.config(text='')
        update_bomb()
        update_score()
        update_display()
        press_return = False


def update_display():
    global bomb
    global score
    if bomb > 50:
        bomb_label.config(image=normal_photo)
    elif 0 < bomb <= 50:
        bomb_label.config(image=no_photo)
    else:
        bomb_label.config(image=bang_photo)
    best_score_label.config(text='High score: ' + str(best_score))
    fuse_label.config(text='Game: ' + str(bomb))
    score_label.config(text='Score: ' + str(score))

    fuse_label.after(100, update_display)


def update_bomb():
    global bomb
    bomb -= 1
    if is_alive():
        fuse_label.after(100, update_bomb)


def update_score():
    global best_score
    global score
    if score >= best_score:
        best_score += 1
    if is_alive():
        score_label.after(3000, update_score)
        score += 1


def click():
    global bomb
    if is_alive():
        if bomb >= 100:
            pass
        else:
            bomb += 1


def is_alive():
    global bomb
    global press_return
    if bomb <= 0:
        label.config(text='Game over - say 8-BIT!')
        press_return = True
        return False
    else:
        return True


root = Tk()  # створення вікна
root.title('8-BIT `press`')  # назва вікна
root.geometry('800x850')  # розміри вікна

label = Label(root, text='Press [enter] to start the game', font=('Comic Sans MS', 12))
label.pack()

fuse_label = Label(root, text='Game: ' + str(bomb), font=('Comic Sans MS', 14))
fuse_label.pack()

score_label = Label(root, text='Score: ' + str(score), font=('Comic Sans MS', 14))
score_label.pack()

best_score_label = Label(root, text='High score: ' + str(best_score), font=('Comic Sans MS', 16))
best_score_label.pack()


no_photo = PhotoImage(file='images/8-BIT_classic.gif')
normal_photo = PhotoImage(file='images/8-BIT_normal.gif')
bang_photo = PhotoImage(file='images/fin_8-BIT.gif')

bomb_label = Label(root, image=normal_photo)
bomb_label.pack()

click_button = Button(root, text='Click me', bg='navy', fg='cyan', width=15,
                      font=('Comic Sans MS', 14), command=click)
click_button.pack()

root.bind('<Return>', start)

root.mainloop()
