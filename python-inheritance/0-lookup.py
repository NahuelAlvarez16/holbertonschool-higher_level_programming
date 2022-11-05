#!/usr/bin/python3
""" 0-lookup Module"""


def lookup(obj):
    """ function that returns the list of available \
        attributes and methods of an object """
    list = []
    for i in dir(obj):
        list.append(i)
    return list
