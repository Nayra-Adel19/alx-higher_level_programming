#!/usr/bin/python3
""" NO -> C -> STR """


def no_c(my_string):
    no_c_string = ""

    for qq in my_string:
        if qq != 'c' and qq != 'C':
            no_c_string += qq

    return no_c_string
