#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """ Check if divisible by 2 """
    new_list = []
    for j in my_list:
        if j % 2 == 0:
            new_list.append(True)
        else:
            new_list.append(False)

    return new_list
