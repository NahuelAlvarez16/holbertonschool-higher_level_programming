#!/usr/bin/python3
""" 5-text_indentation """


def text_indentation(text):
    """ function to print a text """
    line_break = True
    if type(text) != str:
        raise TypeError("text must be a string")
    for c in text:
        if not line_break or c != ' ':
            line_break = False
            print("{}".format(c), end="")
            if c in ".:?":
                print("\n")
                line_break = True
