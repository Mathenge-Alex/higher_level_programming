#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    my_matrix = []

    if len(matrix) > 0:
        for val in matrix[:]:
            my_matrix.append(list(map(lambda x: x ** 2, val)))

    return my_matrix
