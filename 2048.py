import random
from tkinter import *

SIZE = 400  # розмір фрейму(вікна)
GRID_LEN = 4  # розмір сітки 4х4
GRID_PADDING = 10  # відступи між клітинками

BACKGROUND_COLOR_GAME = "#92877d"  # задній фон
BACKGROUND_COLOR_CELL_EMPTY = "#9e948a"  # колір порожньої клітинки

BACKGROUND_COLOR_DICT = {2: "#eee4da", 4: "#ede0c8", 8: "#f2b179",
                         16: "#f59563", 32: "#f67c5f", 64: "#f65e3b",
                         128: "#edcf72", 256: "#edcc61", 512: "#edc850",
                         1024: "#edc53f", 2048: "#edc22e"}  # колір клітинок

CELL_COLOR_DICT = {2: "#776e65", 4: "#776e65", 8: "#f9f6f2", 16: "#f9f6f2",
                   32: "#f9f6f2", 64: "#f9f6f2", 128: "#f9f6f2",
                   256: "#f9f6f2", 512: "#f9f6f2", 1024: "#f9f6f2",
                   2048: "#f9f6f2"}  # колір тексту в клітинках

FONT = ("Verdana", 40, "bold")  # шрифт

KEY_UP = "'w'"  # кнопка вверх
KEY_DOWN = "'s'"  # кнопка вниз
KEY_LEFT = "'a'"  # кнопка вліво
KEY_RIGHT = "'d'"  # кнопка вправо

mainframe = Frame()  # головний фрейм в якому міститься гра
grid_cells = []  # массив відсортованих клітинок
matrix = []  # массив, який буде зберігати клітинки в числовому виді
''


# ШАГ 3
def add_two():  # створює дві 2-йки в довільних клітинках
    a = random.randint(0, len(matrix) - 1)  # генеруємо рандомний стовпчик
    b = random.randint(0, len(matrix) - 1)  # генеруємо рандомний рядок
    while matrix[a][b] != 0:  # знаходження вільної клітинки
        a = random.randint(0, len(matrix) - 1)  # генеруємо рандомний стовпчик
        b = random.randint(0, len(matrix) - 1)  # генеруємо рандомний рядок
    matrix[a][b] = 2  # заповнення вільної клітинки двійкою


# ШАГ 13
def game_state():
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 2048:
                return 'win'
    for i in range(len(matrix) - 1):
        for j in range(len(matrix[0]) - 1):
            if matrix[i][j] == matrix[i + 1][j] or matrix[i][j + 1] == matrix[i][j]:
                return 'not over'
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                return 'not over'
    for k in range(len(matrix) - 1):
        if matrix[len(matrix) - 1][k] == matrix[len(matrix) - 1][k + 1]:
            return 'not over'
    for j in range(len(matrix) - 1):
        if matrix[j][len(matrix) - 1] == matrix[j + 1][len(matrix) - 1]:
            return 'not over'
    return 'lose'


# ШАГ 8
def reverse(mat):  # змінюємо клітинки зліва на право
    new = []  # створення нової матриці
    for i in range(len(mat)):
        new.append([])  # заповенення рядками матрицю
        for j in range(len(mat[0])):
            new[i].append(mat[i][len(mat[0]) - j - 1])  # заповенення оберненими стовпчиками матрицю
    return new  # результат функції


# ШАГ 9
def transpose(mat):  # міняємо місцями i j в клітинках, тобто x на y
    new = []
    for i in range(len(mat[0])):
        new.append([])
        for j in range(len(mat)):
            new[i].append(mat[j][i])
    return new


# ШАГ 5
def cover_up(mat):  # поштовх всіх клітинок вліво, але без змін, якщо клітинки однакові
    new = []  # свторюємо массив в якому буду результат функції
    for i in range(len(mat)):
        new.append([0] * len(mat))  # задання розмірів нової матриці зі старої матриці
    done = False  # збергіє тру чи фолз , якщо вдалося штовхнути вліво то тру, якщо ні то фолз
    for i in range(len(mat)):
        count = 0  # зберігаеємо кі-сть можливих поштовіх вліво в матриці
        for j in range(len(mat)):
            if mat[i][j] != 0:  # якщо клітинка не порожня
                new[i][count] = mat[i][j]  # задаємо їй нові координати, тобто штовхаємо
                if j != count:
                    done = True  # тру якщо вдалося клітинку штовхнути
                count += 1  # додаємо 1, якщо одна клітинка змістилась
    return new, done  # повертаємо два значення(new - нова матриця, після поштовхів, done - резульат в тру чи фолз


# ШАГ 6
def merge(mat):  # зливає клітинки з однаковими числами
    done = False  # зберігає в собі результат зливання клітинок, якщо вийшло то тру, якщо ні то фолз
    for i in range(len(mat)):
        for j in range(len(mat) - 1):  # проходимось по матриці
            if mat[i][j] == mat[i][j + 1] and mat[i][j] != 0:  # перевіряємо якщо клітинка з наступною клітинкою маюьть
                mat[i][j] *= 2  # однакові значення , то ліва множиться на 2, а
                mat[i][j + 1] = 0  # права обнуляється(стає порожньою)
                done = True  # тру - якщо зливання вийшло успішним
    return mat, done  # повертаємо два значення(new - нова матриця, після поштовхів, done - резульат в тру чи фолз)


# ШАГ 11
def up():
    global matrix
    matrix = transpose(matrix)  # мінємо місцями i та j(рядок на стовпчик)
    game, done = cover_up(matrix)  # те саме що в функції left()
    temp = merge(matrix)
    matrix = temp[0]
    done = done or temp[1]
    matrix = cover_up(matrix)[0]
    matrix = transpose(matrix)  # повертаємо матрицю у звичайний стан
    return done


# ШАГ 12
def down():
    global matrix
    matrix = reverse(transpose(matrix))  # міняємо матрицу на обернену матрицу та перставляєм місцями радом зі стовчиком
    matrix, done = cover_up(matrix)  # те саме що в функції left()
    temp = merge(matrix)
    matrix = temp[0]
    done = done or temp[1]
    matrix = cover_up(matrix)[0]
    matrix = transpose(reverse(matrix))  # повертаємо матрицю у звичайний стан
    return done


# ШАГ 7
def left():  # повне зміщення клітинок( не порожніх) вліво в матриці
    global matrix  # глобальна матриця
    matrix, done = cover_up(matrix)  # викликаємо функцію cover_up(поштовх вліво) та результат функції зберігаємо
    temp = merge(matrix)  # в темп зберігаємо результат зливання клітинок з однаковими значеннями
    matrix = temp[0]  # перезаписуємо стару матрицу в нову матриці післу зміщення вліво та зливання клітинок
    done = done or temp[1]  # збергіємо в done  значення True , яке має міститися в одному з цих змінних
    matrix = cover_up(matrix)[0]  # викликаємо ще раз поштовх вліво якщо, при зливанні утворилися пусті клітинки
    return done


# ШАГ 10
def right():  # повне зміщення клітинок( не порожніх) вправо матриці
    global matrix
    matrix = reverse(matrix)  # перезаписуємо матрицу на обернену матрицу
    matrix, done = cover_up(matrix)  # те саме що в функції left()
    temp = merge(matrix)
    matrix = temp[0]
    done = done or temp[1]
    matrix = cover_up(matrix)[0]
    matrix = reverse(matrix)  # повертаємо матрицю у звичайний стан
    return done


# ШАГ 1
def init_grid():  # створює сітки з клітинок
    background = Frame(bg=BACKGROUND_COLOR_GAME, width=SIZE, height=SIZE)  # фрейм яким буде фоном гри
    background.grid()  # додаєм можливість створення елементів в фреймі, тобто створення сітки та клітинок в ній

    for i in range(GRID_LEN):
        grid_row = []
        for j in range(GRID_LEN):  # заповнюємо сітки клітинками
            cell = Frame(background, bg=BACKGROUND_COLOR_CELL_EMPTY, width=SIZE / GRID_LEN,
                         height=SIZE / GRID_LEN)  # створення клітинки
            cell.grid(row=i, column=j, padx=GRID_PADDING, pady=GRID_PADDING)  # задаємо розміри сітки 4х4, та відступи
            t = Label(master=cell, text="", bg=BACKGROUND_COLOR_CELL_EMPTY, justify=CENTER, font=FONT, width=5,
                      height=2)  # створення лейби з відцентровуванням
            t.grid()
            grid_row.append(t)  # створєю стовпчики(4) та записує в список клітинки

        grid_cells.append(grid_row)  # заповює рядки клітинками


# ШАГ 2
def init_matrix():  # створення матриці
    for i in range(GRID_LEN):
        matrix.append([0] * GRID_LEN)  # створення матриці 4х4
    add_two()  # задаєму першу рандомну двійку в матриці
    add_two()  # задаємо другу рандомну двійку в матриці


# ШАГ 4
def update_grid_cells():  # підставляє значення матриці в клітинки та виводити на єкран
    for i in range(GRID_LEN):
        for j in range(GRID_LEN):  # перевіраємо кожну клітинку в матриці
            if matrix[i][j] == 0:  # якщо клітинка порожня
                grid_cells[i][j].configure(text="", bg=BACKGROUND_COLOR_CELL_EMPTY)  # задаємо їй колір пустої клітинки
            else:  # якщо клітинка не порожня, заповнюємо її значенням з матриці
                grid_cells[i][j].configure(text=str(matrix[i][j]), bg=BACKGROUND_COLOR_DICT[matrix[i][j]],
                                           fg=CELL_COLOR_DICT[matrix[i][j]])  # задає значення не порожньої клітинки


def key_down(event):
    key = repr(event.char)
    if key in mainframe.commands:
        done = mainframe.commands[repr(event.char)]()
        if done:
            add_two()
            update_grid_cells()
            if game_state() == 'win':
                grid_cells[1][1].configure(text="Вы", bg=BACKGROUND_COLOR_CELL_EMPTY)
                grid_cells[1][2].configure(text="выграли!", bg=BACKGROUND_COLOR_CELL_EMPTY)
            if game_state() == 'lose':
                grid_cells[1][1].configure(text="Вы", bg=BACKGROUND_COLOR_CELL_EMPTY)
                grid_cells[1][2].configure(text="проиграли!", bg=BACKGROUND_COLOR_CELL_EMPTY)


def main():
    mainframe.master.title('2048')
    mainframe.master.bind("<Key>", key_down)
    mainframe.commands = {KEY_UP: up, KEY_DOWN: down, KEY_LEFT: left, KEY_RIGHT: right}

    init_grid()
    init_matrix()
    update_grid_cells()
    mainloop()


if __name__ == '__main__':  # конструктор( запускає вказані функції )
    main()
