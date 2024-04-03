#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    indx = 0

    try:
        for i in my_list:
            if indx < x:
                print('{}'.format(my_list[indx]), end='')
                indx += 1

        print()
    except TypeError:
        pass
    finally:
        return indx
