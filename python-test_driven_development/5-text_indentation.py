#!/usr/bin/python3
""" 5-text_indentation """


def text_indentation(text):
    """ function to print a text """
    if type(text) != str:
        raise TypeError("text must be a string")
    for c in text:
        print("{}".format(c), end="")
        if c in ".:?":
            print("\n")
    