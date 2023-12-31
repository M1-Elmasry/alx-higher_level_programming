#!/usr/bin/python3
"""
represent a class Rectangle
"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """A representation of a rectangle"""

    def __init__(self, width, height):
        """instantiation of the rectangle"""

        self.integer_validator("width", width)
        self.__width = width

        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """get area of rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """object representation"""
        return f"[{self.__class__.__name__}] {self.__width}/{self.__height}"
