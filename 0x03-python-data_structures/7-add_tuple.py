#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    new_tuple = ()
    tuple_a_1 = tuple_a + (0, 0)
    tuple_b_1 = tuple_b + (0, 0)
    new_tuple = tuple_a_1[0] + tuple_b_1[0], tuple_a_1[1] + tuple_b_1[1]
    return new_tuple
