#!/usr/bin/python3
import sys

if __name__ == '__main__':
    ag_mt = sys.argv
    l_ag_mnt = len(ag_mt) - 1

    if l_ag_mnt > 1:
        print(l_ag_mnt, 'arguments:')
        for i in range(1, l_ag_mnt + 1):
            print('{:d}: {}'.format(i, ag_mt[i]))
    elif l_ag_mnt == 1:
        print(l_ag_mnt, 'argument:')
        for i in range(1, l_ag_mnt + 1):
            print('{:d}: {}'.format(i, ag_mt[i]))
    elif l_ag_mnt == 0:
        print(l_ag_mnt, 'arguments.')
