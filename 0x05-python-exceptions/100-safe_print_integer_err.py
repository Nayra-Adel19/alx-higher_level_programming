#!/usr/bin/python3
""" SAFE """


def safe_print_integer_err(value):

    import sys

    try:
        print("{:d}".format(value))
    except Exception as ff:
        sys.stderr.write("Exception: {}\n".format(ff))
        return False
    else:
        return True
