import unittest
from matrix2 import Matrix


class MatrixTest(unittest.TestCase):
    def test_summa(self):
        self.assertEqual(
            Matrix.__add__(Matrix([[1, 2], [3, 4]]), Matrix([[1, 2], [3, 4]])), [[2, 4], [6, 8]]
        )
        self.assertEqual(
            Matrix.__add__(Matrix([[-1212, 0], [-323, 777], [12, 927]]),
                           Matrix([[-7, 33], [12, 1221], [1, 0]])),
            [[-1219, 33], [-311, 1998], [13, 927]]
        )
        self.assertEqual(
            Matrix.__add__(Matrix([[-7, 33, 212, 322, 324], [12, 0, -9, 1221, 11]]),
                           Matrix([[-8, 2, 4, 333, 432], [121, 10, 66743, 456, 11]])),
            [[-15, 35, 216, 655, 756], [133, 10, 66734, 1677, 22]]
        )

    def test_summa_errors(self):
        self.assertRaises(
            ValueError, Matrix.__add__,
            Matrix([[1, 1, 1], [2, 2, 2]]),
            Matrix([[1, 1, 1], [2, 2, 2], [3, 3, 2]])
        )
        self.assertRaises(
            SyntaxError, Matrix.__add__,
            Matrix([[14324, 1, 341], [234, -9, 2], [-343, 3, 2]]),
            Matrix([[1, 1324, 1], [234, 2], [1, 1, 1, 1]])
        )

    def test_raz(self):
        self.assertEqual(
            Matrix.__sub__(Matrix([[1, 2], [3, 4]]), Matrix([[1, 2], [3, 4]])), [[0, 0], [0, 0]]
        )
        self.assertEqual(
            Matrix.__sub__(Matrix([[-87293, 0], [-323, -777], [124, 927]]),
                           Matrix([[-7, 43134], [4443, 124321], [10, 0]])),
            [[87286, 43134], [4766, 125098], [-114, -927]]
        )
        self.assertEqual(
            Matrix.__sub__(Matrix([[-7, 33, 212, 322], [12, 0, -9, 1221]]),
                           Matrix([[-8, 2, 4, 333], [121, 10, 66743, 456]])),
            [[-1, -31, -208, 11], [109, 10, 66752, -765]]
        )

    def test_raz_errors(self):
        self.assertRaises(
            ValueError, Matrix.__sub__,
            Matrix([[88, 1, 13], [323, 23, 2332]]),
            Matrix([[1, 31, 321], [2, 77, 2], [333, 3, 2]])
        )
        self.assertRaises(
            SyntaxError, Matrix.__sub__,
            Matrix([[43, 7, 341], [234, -9, 2], [555, 3, 2]]),
            Matrix([[1, 30, 1], [0, 0], [1, 1, 9, 1]])
        )

    def test_umn_const(self):
        self.assertEqual(
            Matrix.__mul__(Matrix([[1, 2], [3, 4]]), 291), [[291, 582], [873, 1164]]
        )
        self.assertEqual(
            Matrix.__mul__(Matrix([[1, 2], [3, 4]]), -2192891.5), [[-2192891.5, -4385783.0], [-6578674.5, -8771566.0]]
        )

    def test_umn_matrix(self):
        self.assertEqual(
            Matrix.__mul__(Matrix([[2, 2], [-2, -2], [2, 2]]),
                           Matrix([[2, -2], [2, 2]])),
            [[8, 0], [-8, 0], [8, 0]]
        )
        self.assertEqual(
            Matrix.__mul__(Matrix([[32, 772, 133, 13, 1], [-2, -2, 32983, 0, -323], [2, 2, 21, 3, 0]]),
                           Matrix([[2, -2], [2, 2], [2, 2], [2, 2], [-2, 2]])),
            [[1898, 1774], [66604, 65320], [56, 48]]
        )

    def test_umn_errors(self):
        self.assertRaises(
            ValueError, Matrix.__mul__,
            Matrix([[999, 0], [-2332, -73], [2333, 2323]]),
            Matrix([[7323, -43134], [433, 441], [410, 49]])
        )

    def test_tr(self):
        self.assertEqual(
            Matrix.__invert__(Matrix([[1, 2], [-1, -2], [1, 2]])),
            [[1, -1, 1], [2, -2, 2]]
        )
        self.assertEqual(
            Matrix.__invert__(Matrix([[2939, 32983, 2232], [7, 8, 9]])),
            [[2939, 7], [32983, 8], [2232, 9]]
        )

    def test_tr_errors(self):
        self.assertRaises(
            SyntaxError, Matrix.__invert__,
            Matrix([[783, 23], [-34, 9443], [64, 1223, 3827]])
        )


if __name__ == "__main__":
    unittest.main()
