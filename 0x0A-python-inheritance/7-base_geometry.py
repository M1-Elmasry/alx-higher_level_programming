#!/usr/bin/python3
"""representing an empty class"""


class BaseGeometry:
    """BaseGeometry class"""

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
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
