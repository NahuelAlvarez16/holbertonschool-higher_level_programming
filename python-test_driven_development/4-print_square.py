#!/usr/bin/python3
""" 4-print_square module """


def print_square(size):
    """ function to print a square """
    if type(size) != int and type(size) != float:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
            for x in range(size):
                print("#", end="")
            print()
