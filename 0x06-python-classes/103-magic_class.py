#!/usr/bin/python3
"""Contains the `MagicClass` definition"""
from math import pi


class MagicClass:
    """Computes data for a circle based on a given radius"""

    def __init__(self, radius=0):
        """Checks for exceptions, Instantiates the radius

        Args:
            radius: An int or float value representing the radius of the circle
        """

        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Returns the area of the circle of given radius"""
        return pi * pow(self.__radius, 2)

    def circumference(self):
        """Returns the circumference of a circle of given radius"""
        return 2 * pi * self.__radius
