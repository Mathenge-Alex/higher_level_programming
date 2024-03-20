#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(lambda a: list(map(lambda b: b**2, a)), matrix[:]))
