#!/usr/bin/python3
"""This module the ``0-add_integer`` module

Contained here is the definition of the ``add_integer`` function
"""


def add_integer(a, b=98):
    """Adds two integers

    Args:
        a (Union[int, float]): The first integer to add.
        b (Union[int, float], optional): The second integer to add.
            Default value is 98.

        Returns:
            int: The sum of a and b.

        Raises:
            TypeError: If a or b is not an integer or float.

        Examples:
        >>> add_integer(1, 2)
        3
        >>> add_integer(1.5, 2.5)
        3
        >>> add_integer(1.5, 2)
        3
        >>> add_integer(1)
        99
        >>> add_integer(3, b=4)
        7
        >>> add_integer(-3.2, 45.6)
        42
    """
    # check for invalid types
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")

    # return sum of the integers
    return int(a) + int(b)
