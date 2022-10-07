#!/usr/bin/python3
"""Base class"""


from genericpath import exists
import json
import os


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

    @staticmethod
    def from_json_string(json_string):
        """
        If the json_string is not None, return the json.loads() of
        the json_string, otherwise return an empty list.
        """
        return json.loads(json_string) if json_string is not None else []

    @classmethod
    def create(cls, **dictionary):
        """
        Create a dummy instance of the class, update it with the dictionary,
        and return it.
        """
        dummy = cls(1, 1) if cls.__name__ == "Rectangle" else cls(1)
        dummy.update(**dictionary)
        return dummy

    @staticmethod
    def load_from_file(cls):
        """
        This function creates a list of instances from a json file.
        """
        file_path = cls.__name__ + ".json"
        if os.path.exists(file_path):
            with open(file_path, 'r') as f:
                objs = []
                data = cls.from_json_string(f.read())
                for d in data:
                    objs.append(cls.create(**d))
                return obj
        else:
            return []
