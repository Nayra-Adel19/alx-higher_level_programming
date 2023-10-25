#!/usr/bin/python3
""" PYTHON """


def magic_calculation(a, b):

    from magic_calculation_102 import add, sub

    if a < b:
        c = add(a, b)

        for qq in range(4, 6):
            c = add(c, qq)
        return c
    else:
        return sub(a, b)
