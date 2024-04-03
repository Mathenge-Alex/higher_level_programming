#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    res_lst = []

    for i in range(list_length):
        try:
            res_lst.append(my_list_1[i] / my_list_2[i])
        except ZeroDivisionError:
            res_lst.append(0)
            print('division by 0')
            continue
        except IndexError:
            res_lst.append(0)
            print('out of range')
            continue
        except TypeError:
            res_lst.append(0)
            print('wrong type')
            continue
        finally:
            pass

    return res_lst
