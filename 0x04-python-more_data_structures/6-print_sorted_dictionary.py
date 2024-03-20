#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorted_dict = sorted(a_dictionary.items())

    for j, k in sorted_dict:
        print('{0}: {1}'.format(j, k))
