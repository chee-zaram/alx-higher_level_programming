#!/usr/bin/python3
"""This module the ``3-say_my_name`` module

There is only one function in this module, ``say_my_name`` function
"""


def say_my_name(first_name, last_name=""):
    """Prints out the first and last name

    Args:
        first_name(str): First name
        last_name(str, optional): Last name. Defaults to an empty string

    Raises:
        TypeError: When either the first_name or last_name is not a string

    Examples:
    >>> say_my_name("Chee-zaram", "Okeke")
    My name is Chee-zaram Okeke
    >>> say_my_name("Chee", "Zaram")
    My name is Chee Zaram
    """

    # verify the type of arguments
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
