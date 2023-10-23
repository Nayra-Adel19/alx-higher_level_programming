#!/usr/bin/python3
""" CALCULATION """


def magic_calculation(a, b):

    nresult = 0

    for vv in range(1, 3):

        try:
            if vv > a:
                raise Exception('Too far')
            else:
                nresult += a ** b / vv

        except Exception:
            nresult = b + a
            break
    return nresult
