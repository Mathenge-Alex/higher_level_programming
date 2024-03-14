#!/usr/bin/python3
import sys

if __name__ == '__main__':
    ag_mt = sys.argv
    l_ag_mnt = len(ag_mt)
    sum = 0

    if l_ag_mnt > 1:
        for i in range(1, l_ag_mnt):
            sum += int(ag_mt[i])

    print(sum)
