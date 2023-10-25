#!/usr/bin/python3
""" PYTHON """


def remove_char_at(str, n):
    qq = ''

    for ww in range(len(str)):
        if ww != n:
            qq += str[ww]
    return (qq)
