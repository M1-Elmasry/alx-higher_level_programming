#!/usr/bin/python3
"""a module represent a square class"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """a square class that inherit from Rectangle class"""

    def __init__(self, size):
        """initialization method"""
        self.__size = size
        self.integer_validator("size", self.__size)
        super().__init__(self.__size, self.__size)
