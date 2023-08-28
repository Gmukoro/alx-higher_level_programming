#!/usr/bin/python3
for t in range(100):
    if t == 99:
        print(t)
else:
    print(f"{}".format('0' + str(t) if t < 10 else t), end=", ")
