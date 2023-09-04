class Rectangle:
    """A class representing a rectangle.

    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
    """

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
