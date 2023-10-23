#!/usr/bin/python3
""" SAFE FUNC """


def safe_function(fct, *args):

    import sys

    try:
        return fct(*args)
    except Exception as ff:
        print("Exception: {}".format(ff), file=sys.stderr)
        return None
