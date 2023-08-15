#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return "None"
    else:
        max = my_list[0]
        for t in range(len(my_list)):
            if my_list[t] > max:
                max = my_list[t]
        return max
