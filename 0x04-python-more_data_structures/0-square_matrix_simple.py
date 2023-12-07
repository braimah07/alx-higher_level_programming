#!/usr/bin/python3
def square(x):
    return x ** 2


def square_matrix_simple(matrix=[]):
    return list(map(lambda row: list(map(square, row)), matrix))
