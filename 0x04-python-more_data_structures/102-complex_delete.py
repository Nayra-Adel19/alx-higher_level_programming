#!/usr/bin/python3
""" COMPLEX """


def complex_delete(a_dictionary, value):
    for qq in list(a_dictionary):
        if value == a_dictionary.get(qq):
            del a_dictionary[qq]
    return (a_dictionary)
