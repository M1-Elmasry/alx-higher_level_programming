#!/usr/bin/python3
"""a simple module represent a one class named Square"""


class Square:
    """a square class"""

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    @property
    def size(self):
        """getter of size property"""
        return self.__size

    @size.setter
    def size(self, new_value):
        """setter of size property"""
        if not isinstance(new_value, int):
            raise TypeError("size must be an integer")

        if new_value < 0:
            raise ValueError("size must be >= 0")

        self.__size = new_value

    def area(self):
        """calculate the area of the square"""
        return self.__size**2
