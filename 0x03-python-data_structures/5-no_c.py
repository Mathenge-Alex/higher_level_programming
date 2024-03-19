#!/usr/bin/python3
def no_c(my_string):
    new_str = ''
    for j in my_string:
        if j != 'C' and j != 'c':
            new_str += j

    return new_str
