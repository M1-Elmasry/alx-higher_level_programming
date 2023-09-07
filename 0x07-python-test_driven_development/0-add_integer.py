#!/usr/bin/python3
"""simple function to add two numbers"""


def int_(number):
    """simple funtion to remove float points from number

    Note:
        standard int function can't convert to int if number
        have large floating point

    Args:
        number (float or int): the number that will converted
    """

    if number >= 0:
        number = number - (number % 1)
    else:
        number = number - (number % -1)

    return number


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

    a = int_(a)
    b = int_(b)
    return int(a + b)
