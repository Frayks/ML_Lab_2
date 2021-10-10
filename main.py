import numpy as np
import time

from MyMethods import MyMethods


def print_matrix(matrix):
    for i in range(len(matrix)):
        print(matrix[i])


def test_time_speed():
    a = 100
    b = 100
    matrix1 = np.random.random((a, b))
    matrix2 = np.random.random((b, a))
    vector1 = np.random.random(b)
    vector2 = np.random.random(b)
    print("MyMethods:")
    print("Matrix[{}x{}] multiply matrix[{}x{}]: ".format(a, b, a, b))
    start = time.time()
    MyMethods.matrix_multiply_matrix(matrix1, matrix2)
    end = time.time()
    print("Time: {}".format(end - start))

    print("\nMatrix[{}x{}] multiply vector[{}]: ".format(a, b, b))
    start = time.time()
    MyMethods.matrix_multiply_vector(matrix1, vector1)
    end = time.time()
    print("Time: {}".format(end - start))

    print("\nVector[{}] multiply matrix[{}x{}]: ".format(b, b, a))
    start = time.time()
    MyMethods.vector_multiply_matrix(vector1, matrix2)
    end = time.time()
    print("Time: {}".format(end - start))

    print("\nVector[{}] multiply vector[{}]: ".format(b, b))
    start = time.time()
    MyMethods.vector_multiply_vector(vector1, vector2)
    end = time.time()
    print("Time: {}".format(end - start))

    print("\nNumpy: ")
    print("Matrix[{}x{}] multiply matrix[{}x{}]: ".format(a, b, a, b))
    start = time.time()
    matrix1.dot(matrix2)
    end = time.time()
    print("Time: {}".format(end - start))

    print("\nMatrix[{}x{}] multiply vector[{}]: ".format(a, b, b))
    start = time.time()
    matrix1.dot(vector1)
    end = time.time()
    print("Time: {}".format(end - start))

    print("\nVector[{}] multiply matrix[{}x{}]: ".format(b, b, a))
    start = time.time()
    vector1.dot(matrix2)
    end = time.time()
    print("Time: {}".format(end - start))

    print("\nVector[{}] multiply vector[{}]: ".format(b, b))
    start = time.time()
    vector1.dot(vector2)
    end = time.time()
    print("Time: {}".format(end - start))


def demonstration_of_work():
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
    print("Matrix1: ")
    print_matrix(matrix1)
    print("\nMatrix2: ")
    print_matrix(matrix2)
    print("\nVector1: ")
    print(vector1)
    print("\nVector2: ")
    print(vector2)
    print("\nMatrix1 multiply matrix2: ")
    res_matrix = MyMethods.matrix_multiply_matrix(matrix1, matrix2)
    print_matrix(res_matrix)

    print("\nMatrix1 multiply vector1: ")
    res_vector = MyMethods.matrix_multiply_vector(matrix1, vector1)
    print(res_vector)

    print("\nVector1 multiply matrix2: ")
    res_vector = MyMethods.vector_multiply_matrix(vector1, matrix2)
    print(res_vector)

    print("\nVector1 multiply vector1: ")
    res = MyMethods.vector_multiply_vector(vector1, vector2)
    print(res)


def main():
    test_time_speed()
    # demonstration_of_work()


main()
