#!/usr/bin/python3
""" PYTHON """
for qq in range(122, 96, -1):

    if qq % 2 != 0:
        qq = qq - 32
    print('{:s}'.format(chr(qq)), end='')
