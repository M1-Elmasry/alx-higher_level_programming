#!/usr/bin/python3
"""representing a function is_same_class"""


def is_same_class(obj, a_class):
    """
    check if @obj is an instance from the @a_class

    Args:
        obj (any_type): object
        a_class (class): class

    Return:
     True if @obj is instance from @a_class else False
    """
    if a_class is None:
        return False

    return obj.__class__.__name__ == a_class.__name__
