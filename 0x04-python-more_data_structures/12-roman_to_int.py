#!/usr/bin/python3
""" ROMAN """
""" PYTHON """


def roman_to_int(roman_string):
    if roman_string is None or not isinstance(roman_string, str):
        return 0
    ro = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    sum = 0
    rs = roman_string
    for b in range(len(rs)):
        if b < len(rs) - 1 and ro[rs[b]] < ro[rs[b + 1]]:
            sum -= ro[rs[b]]
        else:
            sum += ro[rs[b]]
    return sum
