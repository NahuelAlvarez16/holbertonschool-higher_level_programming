#!/usr/bin/python3
""" 5-text_indentation """


def text_indentation(text):
    """ function to print a text """
    if type(text) != str:
        raise TypeError("text must be a string")
    print("{}".format(text.rstrip().lstrip()), end="")
    