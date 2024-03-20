#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    target_keys = []
    for k, v in a_dictionary.items():
        if v == value:
            target_keys.append(k)

    for k in target_keys:
        del a_dictionary[k]

    return a_dictionary
