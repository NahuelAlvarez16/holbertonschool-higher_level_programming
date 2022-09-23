#!/usr/bin/python3
"""Square class"""


class Square:
    """ Square """
    def __init__(self, size=0):
        if isinstance(size, int) is False:
            raise TypeError
        if size < 0:
            raise ValueError
        self.__size = size
