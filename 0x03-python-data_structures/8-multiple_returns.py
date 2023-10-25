#!/usr/bin/python3
""" PYTHON MULTIPLE """


def multiple_returns(sentence):

    if not sentence:
        return 0, None

    else:
        return len(sentence), sentence[0]
