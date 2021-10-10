import unittest

from MyMethods import MyMethods


class TestMyMethods(unittest.TestCase):
    matrix1 = [
        [2, 1, 3],
        [3, 2, 1],
        [3, 2, 2],
        [1, 2, 2]
    ]
    matrix2 = [
        [2, 1, 1, 2],
        [3, 2, 2, 1],
        [3, 1, 2, 3]
    ]
    vector1 = [1, 2, 3]
    vector2 = [2, 2, 3]

    def test_matrix_multiply_matrix(self):
        res_matrix = [
            [16, 7, 10, 14],
            [15, 8, 9, 11],
            [18, 9, 11, 14],
            [14, 7, 9, 10]
        ]
        self.assertEqual(MyMethods.matrix_multiply_matrix(self.matrix1, self.matrix2), res_matrix)

    def test_matrix_multiply_vector(self):
        res_vector = [13, 10, 13, 11]
        self.assertEqual(MyMethods.matrix_multiply_vector(self.matrix1, self.vector1), res_vector)

    def test_vector_multiply_matrix(self):
        res_vector = [17, 8, 11, 13]
        self.assertEqual(MyMethods.vector_multiply_matrix(self.vector1, self.matrix2), res_vector)

    def test_vector_multiply_vector(self):
        res = 15
        self.assertEqual(MyMethods.vector_multiply_vector(self.vector1, self.vector2), res)
