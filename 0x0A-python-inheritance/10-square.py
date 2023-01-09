#!/usr/bin/python3
"""Module ``10-square``"""

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Inherits class ``Rectangle``"""

    def __init__(self, size):
        """Initializes instance variables for a Square"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
