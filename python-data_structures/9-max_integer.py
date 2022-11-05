#!/usr/bin/python3
def max_integer(my_list=[]):
    max = None
    for number in my_list:
        if max is None or number > max:
            max = number
    return max
