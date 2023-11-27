#!/usr/bin/python3
"""
func to Write a class LockedClass with no class
dynamically creating new instance attributes,
"""


class LockedClass:
    """ lockedclass """
    __slots__ = ['first_name']
