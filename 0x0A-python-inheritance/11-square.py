#!/usr/bin/python3
"""Module ``11-square`` based on ``10-square``"""

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Inherits class ``Rectangle``"""

    def __init__(self, size):
        """Initializes instance variables for a Square"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """returns a string for the square"""
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
