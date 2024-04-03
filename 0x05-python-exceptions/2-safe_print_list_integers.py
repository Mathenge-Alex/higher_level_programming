#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    to_print = 0

    for i in range(x):
        try:
            if type(my_list[i]) is int and to_print != x:
                print('{:d}'.format(my_list[i]), end='')
                to_print += 1
        except TypeError:
            continue

    print()

    return to_print
