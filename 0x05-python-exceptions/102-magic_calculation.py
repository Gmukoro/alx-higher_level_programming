#!/usr/bin/python3
def magic_calculation(a, b):
    result = 0
    for t in range(1, 3):
        try:
            if t > a:
                raise Exception("Too far")
            result += a ** b / t
        except:
            result = a + b
            break
    return result
