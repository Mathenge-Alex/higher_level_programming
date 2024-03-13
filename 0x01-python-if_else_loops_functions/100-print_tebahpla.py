#!/usr/bin/python3
for j in reversed(range(97, 123)):
    if (j % 2 == 0):
        print('{:c}'.format(j), end='')
    else:
        print('{:c}'.format(j - 32), end='')
