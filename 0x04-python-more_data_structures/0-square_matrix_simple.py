#!/usr/bin/python3
""" SQUARE MATRIX """


def square_matrix_simple(matrix=[]):
    n_matrix = matrix.copy()

    for bb in range(len(matrix)):
        n_matrix[bb] = list(map(lambda n: n ** 2, matrix[bb]))

    return (n_matrix)
