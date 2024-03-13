#!/usr/bin/python3
def print_last_digit(number):
    if number >= 0:
        last_dgt = number % 10
    elif number < 0:
        last_dgt = (number * -1) % 10

    print(last_dgt, end='')
    return last_dgt
