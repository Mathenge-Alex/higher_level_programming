#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """ Create a matrix with list of lists """
    if matrix:
        for elems in matrix:
            j = 1
            length = len(elems)

            for elem in elems:
                if j == length:
                    print('{:d}'.format(elem), end='')
                else:
                    print('{:d}'.format(elem), end=' ')
                j += 1

            print()
