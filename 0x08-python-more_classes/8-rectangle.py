#!/usr/bin/python3
"""a module representing a Rectangle class"""


class Rectangle:
    """A class representing a rectangle.

    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
        number_of_instances (int): number of number_of_instances.
        print_symbol (any type): the symbol that will draw Rectangle with
        when calling __str__.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize a Rectangle object.

        Args:
            width (int, optional): The width of the rectangle. Defaults to 0.
            height (int, optional): The height of the rectangle. Defaults to 0.
        """
        self._is_valid(width, "width")
        self._is_valid(height, "height")
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """get The width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle.

        Args:
            value (int): The new width value
        """
        self._is_valid(value, "width")
        self.__width = value

    @property
    def height(self):
        """get The height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle

        Args:
            value (int): The new height value
        """
        self._is_valid(value, "height")
        self.__height = value

    def area(self):
        """return the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """return perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__width + self.__height) * 2

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """return the biggest rectangle based on the area

        Raises:
            TypeError: when rect_1 or rect_2 is not instances from Rectangle.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")

        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        return max([rect_1, rect_2], key=lambda x: x.area())

    def _is_valid(self, value, dimension):
        """Validate a dimension value.

        Args:
            value (int): The value to be validated
            dimension (str): The name of the dimension

        Raises:
            TypeError: If the value is not an integer
            ValueError: If the value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError(f"{dimension} must be an integer")
        if value < 0:
            raise ValueError(f"{dimension} must be >= 0")

    def __str__(self):
        """draw a rectangle with print_symbol class attribute"""
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            return "\n".join(
                [
                    str(self.print_symbol) * self.__width
                    for _ in range(self.__height)
                ]
            )

    def __repr__(self):
        """return a representation of an instance"""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """make some actions when deleting an instance"""
        print("Bye rectangle...")


my_rectangle_1 = Rectangle(8, 4)
my_rectangle_2 = Rectangle(2, 3)

if my_rectangle_1 is Rectangle.bigger_or_equal(my_rectangle_1, my_rectangle_2):
    print("my_rectangle_1 is bigger or equal to my_rectangle_2")
else:
    print("my_rectangle_2 is bigger than my_rectangle_1")


my_rectangle_2.width = 10
my_rectangle_2.height = 5
if my_rectangle_1 is Rectangle.bigger_or_equal(my_rectangle_1, my_rectangle_2):
    print("my_rectangle_1 is bigger or equal to my_rectangle_2")
else:
    print("my_rectangle_2 is bigger than my_rectangle_1")

