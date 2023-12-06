#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    return list(map(lambda mul: list(map(lambda y: y ** 2 ,mul)), matrix))
