#!/usr/bin/python3
""" BaseGeometry Class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle():
    """ Rectangle """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        __width = width
        self.integer_validator("height", height)
        __height = height