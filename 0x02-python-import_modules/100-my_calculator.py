#!/usr/bin/python3
from sys import argv
from calculator_1 import add, sub, div, mul

if __name__ == '__main__':
    l_ag_mnt = len(argv) - 1

    if l_ag_mnt == 3:
        operator = argv[2]
        arg_a = int(argv[1])
        arg_b = int(argv[3])
        if operator == '+':
            res = add(arg_a, arg_b)
            print('{:d} + {:d} = {:d}'.format(arg_a, arg_b, res))
            exit(0)
        elif operator == '-':
            res = sub(arg_a, arg_b)
            print('{:d} - {:d} = {:d}'.format(arg_a, arg_b, res))
            exit(0)
        elif operator == '*':
            res = mul(arg_a, arg_b)
            print('{:d} * {:d} = {:d}'.format(arg_a, arg_b, res))
            exit(0)
        elif operator == '/':
            res = div(arg_a, arg_b)
            print('{:d} / {:d} = {:d}'.format(arg_a, arg_b, res))
            exit(0)
        else:
            print('Unknown operator. Available operators: +, -, * and /')
            exit(1)
    else:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        exit(1)
