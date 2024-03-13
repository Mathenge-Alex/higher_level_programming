#!/usr/bin/python3
def remove_char_at(str, n):
    new_string = ""

    for j in range(len(str)):
        if j != n:
            new_string += str[j]

    return new_string
