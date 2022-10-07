#!/usr/bin/python3
"""Base class"""


import json


class Base:
    """ Base """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        This function converts a list of dictionaries to a JSON string.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    def save_to_file(cls, list_objs):
        """
        Write a JSON string representation of a list of objects to a file.
        """
        with open(cls.__name__ + ".json", 'w') as f:
            if list_objs is None:
                f.write("[]")
            else:
                objs = []
                for obj in list_objs:
                    objs.append(obj)
                f.write(cls.to_json_string(obj))
