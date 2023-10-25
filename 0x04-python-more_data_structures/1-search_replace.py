#!/usr/bin/python3
""" PYTHON """


def search_replace(my_list, search, replace):
    n_list = []

    for cq in my_list:
        if cq == search:
            n_list.append(replace)

        else:
            n_list.append(cq)

    return n_list
