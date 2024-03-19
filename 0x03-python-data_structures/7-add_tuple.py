#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_a = check_tuple(tuple_a)
    tuple_b = check_tuple(tuple_b)

    return ((tuple_a[0] + tuple_b[0]), (tuple_a[1] + tuple_b[1]))


def check_tuple(any_tuple=()):
    if len(any_tuple) < 2:
        if len(any_tuple) == 1:
            any_tuple = (any_tuple[0], 0)
        elif len(any_tuple) == 0:
            any_tuple = (0, 0)
    elif len(any_tuple) > 2:
        any_tuple = (any_tuple[0], any_tuple[1])

    return any_tuple
