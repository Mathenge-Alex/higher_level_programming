#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """ Replace in a copy """
    copy = my_list.copy()

    if idx < 0 or idx >= len(my_list):
        return copy

    copy[idx] = element
    return copy
