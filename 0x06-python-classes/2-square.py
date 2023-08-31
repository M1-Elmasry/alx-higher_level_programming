#!/usr/bin/python3
"""a simple module represent a one class named Square"""


class Square:
    """a square class"""

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")
