#!/usr/bin/python3
"""The ``101-add_attribute`` module"""


def add_attribute(obj, attr_name, attr_value):
    """Add a new attribute to an object if possible.

    Args:
        obj: The object to add the attribute to.
        attr_name: The name of the attribute to add.
        attr_value: The value of the attribute to add.

    Raises:
        TypeError: if a new attribute could not be added
    """
    # check that the object can store key value pairs like most classes do
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")

    # check if attribute addition is restricted, if so, check if our attribute
    # name is in the list of allowed names
    if hasattr(obj, '__slots__') and attr_name not in obj.__slots__:
        raise TypeError("can't add new attribute")

    setattr(obj, attr_name, attr_value)
