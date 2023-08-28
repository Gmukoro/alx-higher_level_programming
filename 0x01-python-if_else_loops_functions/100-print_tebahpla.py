#!/usr/bin/python3
t = 0
for c in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(c - t)), end="")
    t = 32 if t == 0 else 0
