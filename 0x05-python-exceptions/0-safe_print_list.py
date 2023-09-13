#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    for t in range(x):
        try:
            print(my_list[t], end='')
        except IndexError:
            print()
            return t
    print()
    return x
