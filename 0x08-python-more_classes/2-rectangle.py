#!/usr/bin/python3
"""
This is the ``2-rectangle`` module

It contains the class ``Rectangle``
"""


class Rectangle:
    """class Rectangle that defines a rectangle based on width and height

    Attributes:
        width (int): Width of the rectangle
        height (int): Height of the rectangle
    """

    def __init__(self, width=0, height=0):
        """Initializes a new Rectangle with the given width and height

        Args:
            checkWidth (int): Makes sure width has correct type and value
            checkHeight (int): Makes sure height has correct type and value
            width (int, optional): Width of the Rectangle. Defaults to 0
            height (int, optional): Height of the Rectangle. Defaults to 0
        """
        Rectangle.checkWidth(width)
        self.__width = width
        Rectangle.checkHeight(height)
        self.__height = height

    def __repr__(self):
        """Returns the canonical string representation of ``Rectangle``"""
        return f"Rectangle(width={self.__width}, height={self.__height})"

    @staticmethod
    def checkWidth(width):
        """Makes sure the width has correct type and value

        Args:
            width (int): Width to check

        Raises:
            TypeError: If `width` is not an `int`
            ValueError: If `width` is < 0
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")

    @staticmethod
    def checkHeight(height):
        """Makes sure the height has correct type and value

        Args:
            height (int): Height to check

        Raises:
            TypeError: If height is not an int
            ValueError: If width is < 0
        """
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")

    @property
    def width(self):
        """int: The width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        Rectangle.checkWidth(value)
        self.__width = value

    @property
    def height(self):
        """int: The height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        Rectangle.checkHeight(value)
        self.__height = value

    def area(self):
        """Returns the rectangle area in a given instance"""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the perimeter of the rectangle in a given instance"""
        if self.__width == 0 or self.__height == 0:
            return 0

        return 2 * (self.__width + self.__height)
