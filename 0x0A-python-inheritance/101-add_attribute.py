#!/usr/bin/python3
"""a module represents add_attribute function"""


def add_attribute(obj, attr, value):
    """add new attribute to @obj"""
    if "__dict__" in dir(obj):
        obj.__dict__[attr] = value
    else:
        raise TypeError("can't add new attribute")
