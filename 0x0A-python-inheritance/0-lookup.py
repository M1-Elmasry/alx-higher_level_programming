#!/usr/bin/python3
"""
representing a function that return
method and attributes inside an object
"""


def lookup(obj):
    """
    Args:
        obj (any_type): object

    Return:
        list of methods and and attributes inside @obj
    """
    return dir(obj)
