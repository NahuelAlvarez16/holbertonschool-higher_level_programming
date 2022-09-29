#!/usr/bin/python3
""" MyList Class"""


class MyList(list):
    """ MyList """
    def print_sorted(self):
        list_tmp = self.copy()
        list_tmp.sort()
        print(list_tmp)
