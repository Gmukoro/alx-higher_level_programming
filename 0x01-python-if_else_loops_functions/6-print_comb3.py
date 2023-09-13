#!/usr/bin/python3
for t in range(100):
    if int(t / 10) != t % 10 and int(t / 10) < t % 10:
        print("{}{}".format(int(t / 10), t % 10), end="")
        if (t != 89):
            print(", ", end="")
print("")
