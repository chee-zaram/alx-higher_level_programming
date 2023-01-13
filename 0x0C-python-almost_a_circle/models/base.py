#!/usr/bin/python3
"""Module ``base``"""

import json
# import csv
from os import path


class Base:
    """The base class in the `model` package

    Attributes:
        nb_objects (int): Private class attribute
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes variables for every instance of the `Base` class

        Args:
            id (int): It is assumed that `id` will always be an integer
        """
        if not isinstance(id, int) and id is not None:
            raise TypeError("'id' must be an integer")

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @classmethod
    def create(cls, **dictionary):
        """Gets an instance with all attributes already set

        Args:
            dictionary (dict): A dictionary of instance attributes and values

        Returns:
            An instance with all attributes set
        """
        if cls.__name__ == "Rectangle":
            tempClass = cls(True, True)
        elif cls.__name__ == "Square":
            tempClass = cls(True)

        tempClass.update(**dictionary)
        return tempClass

    @staticmethod
    def from_json_string(json_string):
        """Gets the list of the JSON string representation `json_string`

        Args:
            json_string (str): the JSON string

        Returns:
            The list of the JSON string representation
        """
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances from a file"""

        filename = cls.__name__ + ".json"

        if not path.exists(filename) or not path.isfile(filename):
            return []

        with open(filename, 'r') as file:
            json_string = file.read()

        list_of_dicts = cls.from_json_string(json_string)

        if type(list_of_dicts) != list or not all(
                isinstance(item, dict) for item in list_of_dicts
                ):
            raise TypeError("{} doesn't contain a list of dictionaries".format(
                filename
                ))

        list_of_instances = [cls.create(**a_dict) for a_dict in list_of_dicts]
        return list_of_instances

    @staticmethod
    def to_json_string(list_dictionaries):
        """Gets the JSON string representation of the `list_dictionaries`

        Args:
            list_dictionaries (list): List of dictionaries

        Returns:
            The string representation of the list of dictionaries
        """
        if not list_dictionaries:
            return "[]"

        if type(list_dictionaries) != list or not all(
                type(item) == dict for item in list_dictionaries):
            raise TypeError("'list_dictionaries' must be a list of dicts")

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of `list_objs` to a file

        Args:
            list_objs (list): A list of instances of Base sub-classes
        """

        obj_str = "[]"
        filename = cls.__name__ + ".json"

        if list_objs and type(list_objs) == list:
            obj_str = cls.to_json_string(
                    [obj.to_dictionary() for obj in list_objs]
                    )

        with open(filename, 'w') as obj_file:
            obj_file.write(obj_str)

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serialize in csv

        Args:
            list_objs (list): List of objects
        """
        pass
