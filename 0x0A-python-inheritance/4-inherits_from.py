#!/usr/bin/python3
"""representing a function is_same_class"""


def inherits_from(obj, a_class):
    """
    check if @obj is an instance from the @a_class
    or inherite from any class that @a_class inherits from

    Args:
        obj (any_type): object
        a_class (class): class

    Return:
     True if @obj is instance from @a_class else False
    """
    if a_class is None:
        return False

    obj_class_name = obj.__class__.__name__
    if issubclass(type(obj), a_class) and obj_class_name != a_class.__name__:
        return True
    else:
        return False
