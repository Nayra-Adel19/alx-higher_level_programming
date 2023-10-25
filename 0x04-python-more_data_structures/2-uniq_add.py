#!/usr/bin/python3
""" PYTHON """


def uniq_add(my_list=[]):
    naadd = 0

    for n in set(my_list):
        naadd += n
    return naadd
