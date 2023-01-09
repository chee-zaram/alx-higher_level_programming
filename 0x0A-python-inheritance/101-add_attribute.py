#!/usr/bin/python3
"""The ``101-add_attribute`` module"""


def add_attribute(obj, attr_name, attr_value):
    """Add a new attribute to an object if possible.

    Args:
        obj: The object to add the attribute to.
        attr_name: The name of the attribute to add.
        attr_value: The value of the attribute to add.

    Raises:
        TypeError: if the new attribute could not be added
    """
    if not hasattr(obj, '__slots__') and not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")

    setattr(obj, attr_name, attr_value)
