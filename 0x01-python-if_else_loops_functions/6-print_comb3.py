#!/usr/bin/python3
""" PYTHON """
for qq in range(0, 9):
    uu = qq + 1

    while uu <= 9:
        print("{:d}{:d}".format(qq, uu), end='')
        print(end='\n' if qq == 8 else ", ")
        uu += 1
