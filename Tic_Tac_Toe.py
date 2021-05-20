import random  # Имитация игры с компьютером
from time import sleep  # Для лучшего восприятия хода компьютера

print("""Приветствую Вас, это игра 'Крестики-нолики'!
Чтобы сделать ход, выбери сектор со знаком '-', например, А1. Приятной игры!""")
# Создаём игровое поле
Field = [
    [" ", "A", "B", "C"],
    ["1", "-", "-", "-"],
    ["2", "-", "-", "-"],
    ["3", "-", "-", "-"]
]
# Выводим поле на экран
for i in range(4):
    for j in range(4):
        print(Field[i][j], end=" ")
    print()

Move_my = input("Каков Ваш первый ход?").upper()  # Запрос хода игрока
Not_move_jet = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]  # Создана для выявления ничьей


# Функция срабатывает, если введён некорректный ход
def repeat():
    global Move_my
    Move_my = input("Каков Ваш новый ход?").upper()
    return move(Move_my)


# Ход компьютера и проверка выигрыша
def Move_comp():
    global Field
    Comp_choice = random.choice(Not_move_jet)
    Not_move_jet.remove(Comp_choice)
    print("Ход Компьютера...")
    sleep(0.8)
    if Comp_choice == "A1":
        Field[1][1] = "O"
    elif Comp_choice == "A2":
        Field[2][1] = "O"
    elif Comp_choice == "A3":
        Field[3][1] = "O"
    elif Comp_choice == "B1":
        Field[1][2] = "O"
    elif Comp_choice == "B2":
        Field[2][2] = "O"
    elif Comp_choice == "B3":
        Field[3][2] = "O"
    elif Comp_choice == "C1":
        Field[1][3] = "0"
    elif Comp_choice == "C2":
        Field[2][3] = "O"
    elif Comp_choice == "C3":
        Field[3][3] = "O"
    for i in range(4):
        for j in range(4):
            print(Field[i][j], end=" ")
        print()
    while True:
        if Field[1][1] == Field[1][2] == Field[1][3] == "O":
            print("К сожалению, компьютер победил.")
            break
        elif Field[1][1] == Field[2][1] == Field[3][1] == "O":
            print("К сожалению, компьютер победил.")
            break
        elif Field[1][1] == Field[2][2] == Field[3][3] == "O":
            print("К сожалению, компьютер победил.")
            break
        elif Field[3][1] == Field[2][2] == Field[1][3] == "O":
            print("К сожалению, компьютер победил.")
            break
        else:
            global Move_my
            Move_my = input("Каков Ваш следующий ход?").upper()
            return move(Move_my)


# Декоратор, проверяющий корректность хода
def Can_i_move(move):
    def wraper(*args):
        if Move_my == "A1" or Move_my == "A2" or Move_my == "A3" or Move_my == "B1" or Move_my == "B2" or Move_my == 'B3' or Move_my == "C1" or Move_my == "C2" or Move_my == "C3":
            if Move_my in Not_move_jet:
                move(Move_my)
            else:
                print("Такой ход Уже был!")
                return repeat()
        else:
            print("Такой ход невозможен!")
            return repeat()

    return wraper


# Регистрация хода игрока
@Can_i_move
def move(Move):
    global Field
    Not_move_jet.remove(Move)
    if Move == "A1":
        Field[1][1] = "X"
    elif Move == "A2":
        Field[2][1] = "X"
    elif Move == "A3":
        Field[3][1] = "X"
    elif Move == "B1":
        Field[1][2] = "X"
    elif Move == "B2":
        Field[2][2] = "X"
    elif Move == "B3":
        Field[3][2] = "X"
    elif Move == "C1":
        Field[1][3] = "X"
    elif Move == "C2":
        Field[2][3] = "X"
    elif Move == "C3":
        Field[3][3] = "X"
    for i in range(4):
        for j in range(4):
            print(Field[i][j], end=" ")
        print()
    check()


# Проверка выйгрыша игрока
def check():
    if Field[1][1] == Field[1][2] == Field[1][3] == "X":
        return print("Вы победили! Поздравляем!")
    elif Field[1][1] == Field[2][1] == Field[3][1] == "X":
        return print("Вы победили! Поздравляем!")
    elif Field[1][1] == Field[2][2] == Field[3][3] == "X":
        return print("Вы победили! Поздравляем!")
    elif Field[3][1] == Field[2][2] == Field[1][3] == "X":
        return print("Вы победили! Поздравляем!")
    elif Not_move_jet == []:
        return print("Ничья!")
    else:
        Move_comp()


# Первый вызов функции и начало игрового цикла
move(Move_my)
