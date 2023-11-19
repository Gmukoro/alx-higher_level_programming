#!/usr/bin/python3
""" A function that prints a text with new lines """


def text_indentation(text):
    """ After each . ? and : print 2 new lines

    Args:
        text: the wall of text that we are given

    Return: none, just print
    """
    las = " "
    string = ""
    if text is "":
        print(string, end='')
    if type(text) is not str:
        raise TypeError("text must be a string")
    for i in text:
        if i is las and i is ' ':
            las = i
            continue
        if (las is '.' or las is '?' or las is ':') and i is ' ':
            las = i
            continue
        if i is '.' or i is '?' or i is ':':
            string += i + "\n" + "\n"
            las = i
        else:
            string += i
            las = i
    print(string.rstrip(' '), end="")
