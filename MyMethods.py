class MyMethods:

    @staticmethod
    def matrix_multiply_matrix(matrix1, matrix2):
        res_matrix = [[0 for _ in range(len(matrix1))] for _ in range(len(matrix2[0]))]
        for i in range(len(matrix1)):
            for j in range(len(matrix2[0])):
                for r in range(len(matrix1[0])):
                    res_matrix[i][j] += matrix1[i][r] * matrix2[r][j]
        return res_matrix

    @staticmethod
    def matrix_multiply_vector(matrix, vector):
        res_vector = [0 for _ in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                res_vector[i] += matrix[i][j] * vector[j]
        return res_vector

    @staticmethod
    def vector_multiply_matrix(vector, matrix):
        res_vector = [0 for _ in range(len(matrix[0]))]
        for j in range(len(matrix[0])):
            for i in range(len(matrix)):
                res_vector[j] += matrix[i][j] * vector[i]
        return res_vector

    @staticmethod
    def vector_multiply_vector(vector1, vector2):
        res = 0
        for i in range(len(vector1)):
            res += vector1[i] * vector2[i]
        return res
