#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    list_keys = list(a_dictionary.keys())
    for value_one in list_keys:
        if value == a_dictionary.get(value_one):
            del a_dictionary[value_one]
    return (a_dictionary)
