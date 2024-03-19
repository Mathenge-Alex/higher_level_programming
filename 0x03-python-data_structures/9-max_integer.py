#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None

    max_int = min(my_list)
    for j in my_list:
        if j > max_int:
            max_int = j

    return max_int
