#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    """
    Multiply all values by 2 in a dictionary
    """
    new_dictionary = a_dictionary.copy()

    for j, k in new_dictionary.items():
        new_dictionary[j] = k * 2

    return new_dictionary
