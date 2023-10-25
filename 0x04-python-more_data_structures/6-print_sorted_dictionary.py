#!/usr/bin/python3
""" PYTHON """


def print_sorted_dictionary(a_dictionary):
    for qq in sorted(a_dictionary.keys()):
        print("{:s}: {}".format(qq, a_dictionary.get(qq)))
