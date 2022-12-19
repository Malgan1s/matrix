class Matrix:
    """
    Создание класса матриц
    """

    def __init__(self, matrix):
        self.matrix = matrix

    def __add__(self, other):
        """
        метод __add__ отвечает за сложение матриц
        Вызывается автоматически, когда задаётся команда "Matrix_1 + Matrix_2" (сумма матриц)
        :param self - первая матрица, other - вторая матрица:
        :return: с - сумма двух матриц
        :raise: вызывает исключения, если одна из матриц задана неверно или если их размерность не совпадает
        """
        a = self.matrix
        b = other.matrix
        if len(a) == len(b):
            n = len(a[0])
            for i in a:
                if len(i) != n:
                    raise SyntaxError("Первая матрица задана неверно!")
            for g in b:
                if len(g) != n:
                    raise SyntaxError("Вторая матрица задана неверно!")
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

    def __sub__(self, other):
        """
        метод __sub__ отвечает за вычитание.
        вызывается автоматически, когда задаётся команда "Matrix_1 - Matrix_2" (разность матриц)
        :param self - первая матрица, other - вторая матрица:
        :return: с - разность двух матриц
        :raise: вызывает исключения, если одна из матриц задана неверно или если их размерность не совпадает
        """
        a = self.matrix
        b = other.matrix
        if len(a) == len(b):
            n = len(a[0])
            for i in a:
                if len(i) != n:
                    raise SyntaxError("Первая матрица задана неверно!")
            for g in b:
                if len(g) != n:
                    raise SyntaxError("Вторая матрица задана неверно!")
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

    def __mul__(self, other):
        """
        метод __mul__ отвечает за умножение матрицы на число или на другую матрицу.
        Вызывается автоматически, когда задаётся команда "Matrix * const" или "Matrix_1 * Matrix_2"
        :param self - первая матрица, other - любое число или вторая матрица
        :return: result - произведение матрицы на число, c - произведение двух матриц
        :raise: вызывает исключение, если перемножить матрицы невозможно
        """
        a = self.matrix
        if isinstance(other, int) or isinstance(other, float):
            result = []
            nb = []
            for i in range(0, len(a)):
                for g in range(0, len(a[0])):
                    nb.append(a[i][g] * other)
                    if len(nb) == len(a[0]):
                        result.append(nb)
                        nb = []
            return result
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

    def __xor__(self, other):
        """
        метод __xor__ отвечает за транспонирование матрицы.
        Вызывается автоматически, когда задаётся команда Matrix_1 ^ Matrix_2
        :param self - заданная матрица
        :return: tr_a - транспонированная матрица
        """
        a = self.matrix
        n = len(a[0])
        for i in a:
            if len(i) != n:
                raise SyntaxError("Матрица задана неверно!")
        tr_a = [[0 for j in range(len(a))] for i in range(len(a[0]))]
        for i in range(0, len(a)):
            for g in range(0, len(a[0])):
                tr_a[g][i] = a[i][g]
        return tr_a
