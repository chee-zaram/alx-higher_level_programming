#!/usr/bin/python3
"""Module ``9-rectangle``"""
baseG = __import__("7-base_geometry").BaseGeometry


class Rectangle(baseG):
    """Inherits baseG and initializes a Rectangle"""

    def __init__(self, width, height):
        """Initializes instance of `BaseGeometry`"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def __str__(self):
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)

    def area(self):
        """Returns the area of the rectangle"""
        return self.__width * self.__height
