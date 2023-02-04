#!/usr/bin/python3
"""Module ``base``"""

import json
import csv
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
            id (int): It is assumed that `id` will always be an integer.
                Defaults to `None`
        """
        if id is not None and type(id) != int:
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
            temp_instance = cls(1, 1)
        elif cls.__name__ == "Square":
            temp_instance = cls(1)
        else:
            raise AttributeError("{} is not a valid class".format(
                cls.__name__))

        temp_instance.update(**dictionary)
        return temp_instance

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

        if type(json_string) != str:
            raise TypeError("'json_string' must be a string")

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
                type(item) == dict for item in list_of_dicts
                ):
            raise TypeError("{} doesn't contain a list of dictionaries".format(
                filename
                ))

        list_of_instances = [cls.create(**a_dict) for a_dict in list_of_dicts]

        return list_of_instances

    @classmethod
    def load_from_file_csv(cls):
        """Deserialize key/value pairs for several instances of `Base`"""

        filename = cls.__name__ + ".csv"
        list_of_instances = []
        if not path.exists(filename) or not path.isfile(filename):
            return list_of_instances

        with open(filename, 'r') as csvfile:
            if cls.__name__ == "Rectangle":
                attrs = ("id", "width", "height", "x", "y")
            elif cls.__name__ == "Square":
                attrs = ("id", "size", "x", "y")
            else:
                return list_of_instances

            rows = csv.reader(csvfile, delimiter=',')
            for idx, row in enumerate(rows):
                if idx == 0:
                    continue

                temp_instance = cls(1, 1)
                for attr_idx, attr_value in enumerate(row):
                    if attr_idx == len(attrs):
                        raise AttributeError("Too many attributes given")

                    # if rows not in attrs:
                    #     raise AttributeError("Invalid attribute given")

                    if attr_value:
                        try:
                            val = int(attr_value)
                            setattr(temp_instance, attrs[attr_idx], int(val))
                        except (TypeError, ValueError):
                            raise

                list_of_instances.append(temp_instance)

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

        if list_objs and type(list_objs) == list and all(
                type(obj) == cls for obj in list_objs
                ):
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

        filename = cls.__name__ + ".csv"

        if list_objs and type(list_objs) == list and all(
                type(obj) == cls for obj in list_objs
                ):
            obj_dicts = [obj.to_dictionary() for obj in list_objs]
        else:
            list_objs = []
            obj_dicts = [{}]

        with open(filename, 'w', newline='') as csvfile:
            if cls.__name__ == "Rectangle":
                attrs = ("id", "width", "height", "x", "y")
            elif cls.__name__ == "Square":
                attrs = ("id", "size", "x", "y")
            else:
                raise AttributeError("{} is not a valid class".format(
                    cls.__name__))

            csv.DictWriter(csvfile, fieldnames=attrs).writeheader()
            csv.DictWriter(csvfile, fieldnames=attrs).writerows(obj_dicts)
