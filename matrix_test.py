import unittest

from matrix import Matrix
from matrix import main


class MatrixTest(unittest.TestCase):
    def test_main(self):
        self.assertEqual(main(), print("Конец выполнения программы"))

    def test_summa(self):
        self.assertEqual(Matrix.__add__(Matrix([[1, 2], [3, 4]]), Matrix([[1, 2], [3, 4]])), [[2, 4], [6, 8]])
        self.assertEqual(Matrix.__add__(Matrix([[-21, 23], [33, 0]]), Matrix([[12, -2], [33, 43]])),
                         [[-9, 21], [66, 43]])
        self.assertEqual(Matrix.__add__(Matrix([[123, -2313, 432], [0, 213, 3], [44, 33, 22]]),
                                        Matrix([[231, -3213, 323], [54, -434, 432], [44, 43, 2]])),
                         [[354, -5526, 755], [54, -221, 435], [88, 76, 24]])

    def test_raz(self):
        self.assertEqual(Matrix.__sub__(Matrix([[1, 2], [3, 4]]), Matrix([[1, 2], [3, 4]])), [[0, 0], [0, 0]])
        self.assertEqual(Matrix.__sub__(Matrix([[123, 0], [-32132, 321]]), Matrix([[123, 543], [123, -43]])),
                         [[0, -543], [-32255, 364]])
        self.assertEqual(Matrix.__sub__(Matrix([[123, -329, 321], [0, 3, 23], [-33, 23, 312]]),
                                        Matrix([[3123, 3, 2], [233, -3233, 232333], [2, 2213, -1]])),
                         [[-3000, -332, 319], [-233, 3236, -232310], [-35, -2190, 313]])

    def test_mn(self):
        self.assertEqual(Matrix.__and__(Matrix([[1, 2], [3, 4]]), 3), [[3, 6], [9, 12]])
        self.assertEqual(Matrix.__and__(Matrix([[1, 2], [3, 4]]), 123), [[123, 246], [369, 492]])
        self.assertEqual(Matrix.__and__(Matrix([[123, 123, 43234], [2344, -43, 0], [432, 423, 123]]), -1111),
                         [[-136653, -136653, -48032974], [-2604184, 47773, 0], [-479952, -469953, -136653]])


if __name__ == "__main__":
    unittest.main()
