#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0

    return sum([multiply(j[0], j[1]) for j in my_list]) / sum(j[1] for j in my_list)


def multiply(j, k):
    return j * k
