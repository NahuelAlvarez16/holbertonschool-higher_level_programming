#!/usr/bin/python3
""" Rectangle module """


class Rectangle:
    """ Rectangle class """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.width * self.height

    def perimeter(self):
        if not self.width or not self.height:
            return 0
        return (self.width + self.height) * 2

    def __str__(self):
        str = ""
        if self.height and self.width:
            for h in range(self.height):
                if h > 0:
                    str += '\n'
                for w in range(self.width):
                    if type(self.print_symbol) != str:
                        self.print_symbol = str(self.print_symbol)
                    str += self.print_symbol
        return str

    def __repr__(self):
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
