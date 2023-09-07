#!/usr/bin/python3
"""simple function to add two numbers"""


def add_integer(a, b=98):
    """add a with b

    Args:
        a (int): first number
        b (int): second number with default value 98

    Raises:
        TypeError: if a or b is not int
    """

    if not isinstance(a, int):
        raise TypeError("a must be an integer")
    if not isinstance(b, int):
        raise TypeError("b must be an integer")

    return a + b
