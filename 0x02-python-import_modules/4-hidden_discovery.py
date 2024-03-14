#!/usr/bin/python3
import hidden_4

if __name__ == '__main__':
    prog_names = dir(hidden_4)

    for j in range(len(prog_names)):
        if prog_names[j][:2] != '__':
            print(prog_names[j])
