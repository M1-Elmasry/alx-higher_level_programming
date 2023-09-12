#!/usr/bin/python3
"""
representing an empty class
"""


class BaseGeometry:
    """
    BaseGeometry class
    """

    def area(self):
        """raise an Exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        validate @value

        Args:
            name (str): name of geometry
            value (int): value of the geometry

        Raise:
            TypeError: when name is not an integer
            ValueError: when value is less than or equal 0
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
