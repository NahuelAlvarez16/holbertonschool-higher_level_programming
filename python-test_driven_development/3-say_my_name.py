#!/usr/bin/python3
""" 3-say_my_name module """


import string
from typing import Type


def say_my_name(first_name, last_name=""):
    """ function to concat a name with last name"""
    print(type(first_name))
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    if type(last_name) != str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))