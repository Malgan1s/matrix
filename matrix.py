## Документация.
#  Установлен модуль numpy
import numpy as np


## функция main отвечает за создание интерактивного меню
def main():
    global a
    global b
    global c
    # Пока не будет произведён выход из меню, cледующие порядковые номера отчечает за такие действия, как:
    # 1 - Введение количества матриц
    # 2 - Сложение двух матриц
    # 3 - Вычитание двух матриц
    # 4 - Умножение матрицы на число
    # 5 - Транспонирование матрицы
    cmd = str(input("Введите команду: "))
    while cmd != "Exit":
        if cmd == "1":
            cmd = str(input("Введите количество матриц, которые требуется задать: "))
            if cmd == "1":
                a = set_matrix_a()
                c = set_matrix_c
            elif cmd == "2":
                a = set_matrix_a()
                b = set_matrix_b()
                c = set_matrix_c
            else:
                print("Введите значение, не превышающие 2")
        elif cmd == "2":
            try:
                print("a + b =")
                suma = a + b
                print(suma)
            except NameError:
                print("Ошибка! Сначала задайте матрицы!")
        elif cmd == "3":
            try:
                print("a - b =")
                raz = a - b
                print(raz)
            except NameError:
                print("Ошибка! Сначала задайте матрицы!")
        elif cmd == "4":
            try:
                print("a & c =")
                pr_cst = a & c
                print(pr_cst)
            except NameError:
                print("Ошибка! Сначала задайте матрицу!")
        elif cmd == "5":
            try:
                print("a / a =")
                tra = a / a
                print(tra)
            except NameError:
                print("Ошибка! Сначала задайте матрицу!")
        else:
            print("Такой комманды нет")
        cmd = str(input("Введите команду: "))
    return print("Конец выполнения программы")


## Создание класса матриц
class Matrix:

    def __init__(self, matrix):
        self.matrix = matrix

    # метод __add__ отвечает за сложение. Вызывается автоматически, когда задаётся команда a + b (сложение матриц)
    def __add__(self, other):
        A = self.matrix
        B = other.matrix
        C = A
        n = len(self.matrix)
        kol_i = 0
        kol_g = 0
        for i in range(len(A)):
            kol_i += 1
        for g in range(len(B)):
            kol_g += 1
        if kol_i != kol_g:
            raise ValueError("Размерность матриц не совпадает!")
        for i in range(n):
            for g in range(n):
                C[i][g] = A[i][g] + B[i][g]
        return C

    # метод __sub__ отвечает за вычитание. Вызывается автоматически, когда задаётся команда a - b (разность матриц)
    def __sub__(self, other):
        A = self.matrix
        B = other.matrix
        C = A
        n = len(self.matrix)
        kol_i = 0
        kol_g = 0
        for i in range(len(A)):
            kol_i += 1
        for g in range(len(B)):
            kol_g += 1
        if kol_i != kol_g:
            raise ValueError("Размерность матриц не совпадает!")
        for i in range(n):
            for g in range(n):
                C[i][g] = A[i][g] - B[i][g]
        return C

    # метод __and__ отвечает за умножение матрицы на константу. Вызывается автоматически, когда задаётся команда a & с
    def __and__(self, other):
        A = self.matrix
        const = int(input("Введите любое число: "))
        C = A
        n = len(self.matrix)
        for i in range(n):
            for g in range(n):
                C[i][g] = A[i][g] * const
        return C

    # метод __truediv__ отвечает за транспонирование матрицы. Вызывается автоматически, когда задаётся команда a / a
    def __truediv__(self, other):
        A = self.matrix
        C = np.matrix(A)
        C_t = C.transpose()
        return C_t


## Функция set_matrix_a задаёт матрицу a
def set_matrix_a():
    itg = []
    stk = int(input("Введите количество строк для матрицы: "))
    stb = int(input("Введите количество cтолбцов для матрицы: "))
    for i in range(stk):
        itg.append([0] * stb)
    for i in range(stk):
        for g in range(stb):
            itg[i][g] = int(input())
    a = itg
    print(a)
    a = Matrix(a)
    return a


## Функция set_matrix_b задаёт матрицу b
def set_matrix_b():
    itg = []
    stk = int(input("Введите количество строк для матрицы: "))
    stb = int(input("Введите количество cтолбцов для матрицы: "))
    for i in range(stk):
        itg.append([0] * stb)
    for i in range(stk):
        for g in range(stb):
            itg[i][g] = int(input())
    b = itg
    print(b)
    b = Matrix(b)
    return b


## Функция set_matrix_c задаёт константу
def set_matrix_c():
    c = int(input())
    c = Matrix(c)
    return c


main()
