#!/usr/bin/python3
"""This is the ``square`` module

Contained here is the sub-class ``Square`` inheriting from class ``Rectangle``
in the ``rectangle`` module, all in the ``models`` package
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """This class defines a square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes attributes for each instance of the `Square` class

        This method uses `super().__init__`

        Args:
            size (int): Size of the square
            x (int): Point on the x axis
            y (int): Point on the y axis
            id (int): Identification number of the `Square` instance
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns the string representation of the `Square` instance"""

        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(
                self.id, self.x, self.y, self.width
                )

    @property
    def size(self):
        """Getter function for the size of the `Square` instance

        Args:
            value (int): Value of the width and height
        """
        return self.width

    @size.setter
    def size(self, value):
        self.validate_width_and_height(value, "width")
        self.width = value
        self.validate_width_and_height(value, "height")
        self.height = value

    def to_dictionary(self):
        """Returns the dictionary representation of a `Square` instance"""

        return {
                'id': self.id,
                'size': self.size,
                'x': self.x,
                'y': self.y,
            }

    def update(self, *args, **kwargs):
        """Assigns values to attributes for a `Square` instance

        Args:
            args (list): List of arguments
            kwargs (dict): Key word arguments
        """

        attrs = ('id', 'size', 'x', 'y')
        if args and len(args) > 0 and len(args) <= len(attrs):
            for idx in range(len(args)):
                setattr(self, attrs[idx], args[idx])
        elif kwargs and len(kwargs) > 0:
            for attr in filter(lambda attr: attr in kwargs, attrs):
                setattr(self, attr, kwargs[attr])
