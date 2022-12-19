## Документация.
## Создание класса матриц
class Matrix:

    def __init__(self, matrix):
        self.matrix = matrix

    # метод __add__ отвечает за сложение матриц
    # Вызывается автоматически, когда задаётся команда "Matrix_1 + Matrix_2" (сумма матриц)
    def __add__(self, other):
        a = self.matrix
        b = other.matrix
        if len(a) == len(b):
            n = len(a[0])
            for i in a:
                if len(i) != n:
                    raise ValueError("Первая матрица задана неверно!")
            for g in b:
                if len(g) != n:
                    raise ValueError("Вторая матрица задана неверно!")
            c = []
            nb = []
            for i in range(len(a)):
                for g in range(len(a[0])):
                    nb.append(b[i][g] + a[i][g])
                    if len(nb) == len(a[0]):
                        c.append(nb)
                        nb = []
            return c
        else:
            raise ValueError("Размерность матриц не совпадает!")

    # метод __sub__ отвечает за вычитание.
    # Вызывается автоматически, когда задаётся команда "Matrix_1 - Matrix_2" (разность матриц)
    def __sub__(self, other):
        a = self.matrix
        b = other.matrix
        if len(a) == len(b):
            n = len(a[0])
            for i in a:
                if len(i) != n:
                    raise ValueError("Первая матрица задана неверно!")
            for g in b:
                if len(g) != n:
                    raise ValueError("Вторая матрица задана неверно!")
            c = []
            nb = []
            for i in range(len(a)):
                for g in range(len(a[0])):
                    nb.append(b[i][g] - a[i][g])
                    if len(nb) == len(a[0]):
                        c.append(nb)
                        nb = []
            return c
        else:
            raise ValueError("Размерность матриц не совпадает!")

    # метод __mul__ отвечает за умножение матрицы на число или на другую матрицу.
    # Вызывается автоматически, когда задаётся команда "Matrix * const" или "Matrix_1 * Matrix_2"
    def __mul__(self, other):
        a = self.matrix
        # первая часть __mul__ считает умножение матрицы на число
        if isinstance(other, int) or isinstance(other, float):
            c = []
            nb = []
            for i in range(0, len(a)):
                for g in range(0, len(a[0])):
                    nb.append(a[i][g] * other)
                    if len(nb) == len(a[0]):
                        c.append(nb)
                        nb = []
            return c
        # вторая часть __mul__ считает умножение матрицы на другую матрицу
        else:
            b = other.matrix
            n = 0
            for i in range(0, len(b)):
                for g in range(0, len(b[0])):
                    n += 1
            if len(a[0]) == n / len(b[0]):
                c = []
                for i in range(len(a)):
                    res = []
                    for g in range(len(b[0])):
                        nb = 0
                        for e in range(len(a[0])):
                            m = a[i][e] * b[e][g]
                            nb += m
                        res.append(nb)
                    c.append(res)
                return c
            else:
                raise ValueError("Перемножить данные матрицы невозможно!")

    # метод __xor__ отвечает за транспонирование матрицы.
    # Вызывается автоматически, когда задаётся команда Matrix_1 ^ Matrix_2
    def __xor__(self, other):
        a = self.matrix
        trans_a = [[0 for j in range(len(a))] for i in range(len(a[0]))]
        for i in range(0, len(a)):
            for g in range(0, len(a[0])):
                trans_a[g][i] = a[i][g]
        return trans_a
