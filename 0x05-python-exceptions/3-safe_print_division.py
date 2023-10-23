#!/usr/bin/python3


def safe_print_division(a, b):

    ss = 0

    try:
        ss = a / b
    except ZeroDivisionError:
        ss = None
    finally:
        print("Inside result: {}".format(ss))

    return ss
