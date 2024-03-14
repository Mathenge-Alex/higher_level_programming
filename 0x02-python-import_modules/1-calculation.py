#!/usr/bin/python3
from calculator_1 import add, sub, div, mul

def calc_ops():
    a = 10
    b = 5
    print(f"{a} + {b} = {add(a, b)}")
    print(f"{a} - {b} = {sub(a, b)}")
    print(f"{a} * {b} = {mul(a, b)}")
    print(f"{a} / {b} = {div(a, b)}")

if __name__ == '__main__':
    calc_ops()
