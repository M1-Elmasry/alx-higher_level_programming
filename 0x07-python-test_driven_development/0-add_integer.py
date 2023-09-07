#!/usr/bin/python3
"""simple function to add two numbers"""


def add_integer(a, b=98):
    """add a with b

    Args:
        a (int): first number
        b (int): second number with default value 98

    Raises:
        TypeError: if a or b is not int and not float
    """

    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")

    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)

    return int(a) + int(b)
