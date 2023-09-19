#!/usr/bin/python3
"""Represents a square class."""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Represents a Square.

    This class inherits from the `Rectangle` class and extends it to
    represent a square with specific properties:
    side length, x-coordinate, y-coordinate, and an ID.

    Attributes:
        size (int): The side length of the square.
        x (int): The x-coordinate of the square's position.
        y (int): The y-coordinate of the square's position.
        id (int): The unique identifier of the square.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Args:
            size (int): The side length of the square.
            x (int, optional):
                The x-coordinate of the square's position (default is 0).
            y (int, optional):
                The y-coordinate of the square's position (default is 0).
            id (int, optional):
                The unique identifier of the square (default is None
                and the class will give it it's order in instances).
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """getter to the size property"""
        return self.width

    @size.setter
    def size(self, value):
        """
        Set the size of the square.

        Args:
            value (int): The new height value.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        update instance attributes

        Args:
            *args: list of new attribute values
            Note: not neccessary to update all attributes
            can update id only, size only, etc.., or all
                1st: id
                2nd: size
                4th: x
                5th: y

            **kwargs: key/value pairs to update attribute values
        """
        len_args = len(args)
        keys_kwargs = kwargs.keys()

        if len_args > 0:
            self.id = args[0]
            if len_args > 1:
                self.size = args[1]
            if len_args > 2:
                self.x = args[2]
            if len_args > 3:
                self.y = args[3]
        else:
            if "id" in keys_kwargs:
                self.id = kwargs["id"]
            if "size" in keys_kwargs:
                self.size = kwargs["size"]
            if "x" in keys_kwargs:
                self.x = kwargs["x"]
            if "y" in keys_kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """return dictionary representation to the instance"""
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y,
        }

    def __str__(self):
        """return string representation to the instance"""
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(
            self.id,
            self.x,
            self.y,
            self.width,
        )
