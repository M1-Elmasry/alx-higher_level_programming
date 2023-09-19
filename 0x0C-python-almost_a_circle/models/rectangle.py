#!/usr/bin/python3
"""representing the rectangle class"""

from models.base import Base


class Rectangle(Base):
    """
    Represents a Rectangle.

    This class inherits from the `Base` class and extends it to
    represent a rectangle with specific properties:
    width, height, x-coordinate, y-coordinate, and an ID.

    Instance Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
        x (int): The x-coordinate of the rectangle's position.
        y (int): The y-coordinate of the rectangle's position.
        id (int): The unique identifier of the rectangle.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a new instance of the Rectangle class.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int, optional):
                The x-coordinate of the rectangle's position (default is 0).
            y (int, optional):
                The y-coordinate of the rectangle's position (default is 0).
            id (int, optional):
                The unique identifier of the rectangle (default is None).

        Raises:
            TypeError: If any of the dimension values
            (width, height, x, y) is not an integer.

            ValueError: If any of the dimension values
            (width, height) is less than or equal 0
            or the coordinate values (x, y) is less than 0.
        """
        self.__is_valid_dimension(width, "width")
        self.__is_valid_dimension(height, "height")
        self.__is_valid_coordinate(x, "x")
        self.__is_valid_coordinate(y, "y")
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """Get the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the width of the rectangle.

        Args:
            value (int): The new width value.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        self.__is_valid_dimension(value, "width")
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the height of the rectangle.

        Args:
            value (int): The new height value.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        self.__is_valid_dimension(value, "height")
        self.__height = value

    @property
    def x(self):
        """Get the x-coordinate of the rectangle's position."""
        return self.__x

    @x.setter
    def x(self, value):
        self.__is_valid_coordinate(value, "x")
        self.__x = value

    @property
    def y(self):
        """Get the y-coordinate of the rectangle's position."""
        return self.__y

    @y.setter
    def y(self, value):
        self.__is_valid_coordinate(value, "y")
        self.__y = value

    def __is_valid_dimension(self, value, dimension):
        """
        Validate a dimension value.

        Args:
            value (int): The value to be validated.
            dimension (str): The name of the dimension.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{dimension} must be an integer")
        if value <= 0:
            raise ValueError(f"{dimension} must be > 0")

    def __is_valid_coordinate(self, value, coordinate):
        """
        Validate a coordinate value.

        Args:
            value (int): The value to be validated.
            coordinate (str): The name of the coordinate.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{coordinate} must be an integer")
        if value < 0:
            raise ValueError(f"{coordinate} must be >= 0")

    def area(self):
        """return the area of the rectangle"""
        return self.width * self.height

    def display(self):
        """
        draw rectangle with hashes (#)
        according to it's (width, height, x, y)
        """
        print("\n" * self.y, end="")
        print(
            "\n".join(
                [" " * self.x + "#" * self.width for _ in range(self.height)]
            )
        )

    def update(self, *args, **kwargs):
        """
        update instance attributes

        Args:
            *args: list of new attribute values
            Note: not neccessary to update all attributes
            can update id only, width only, etc.., or all
                1st: id
                2nd: width
                3rd: height
                4th: x
                5th: y

            **kwargs: key/value pairs to update attribute values
        """
        len_args = len(args)
        keys_kwargs = kwargs.keys()

        if len_args > 0:
            self.id = args[0]
            if len_args > 1:
                self.width = args[1]
            if len_args > 2:
                self.height = args[2]
            if len_args > 3:
                self.x = args[3]
            if len_args > 4:
                self.y = args[4]
        else:
            if "id" in keys_kwargs:
                self.id = kwargs["id"]
            if "width" in keys_kwargs:
                self.width = kwargs["width"]
            if "height" in keys_kwargs:
                self.height = kwargs["height"]
            if "x" in keys_kwargs:
                self.x = kwargs["x"]
            if "y" in keys_kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """return dictionary representation to the instance"""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y,
        }

    def __str__(self):
        """return string representation to the instance"""
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(
            self.id,
            self.x,
            self.y,
            self.width,
            self.height,
        )
