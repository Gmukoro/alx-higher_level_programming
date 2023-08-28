#!/usr/bin/python3
def uppercase(str):
    for t in range(len(str)):
        if ord(str[t]) >= 97 and ord(str[t]) < 123:
            letter = 32
        else:
            letter = 0
        print("{:c}".format(ord(str[t]) - letter), end='')
    print()
