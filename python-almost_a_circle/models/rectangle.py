#!/usr/bin/python3
"""Rectangle class that inherits from Base"""
from models.base import Base


class Rectangle(Base):
    """ Rectangle """

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def update(self, *args, **kwargs):
        """
        It updates the values of the class Rectangle
        """
        if len(args) > 0:
            for idx, arg in enumerate(args):
                if idx == 0:
                    self.id = arg
                elif idx == 1:
                    self.width = arg
                elif idx == 2:
                    self.height = arg
                elif idx == 3:
                    self.x = arg
                elif idx == 4:
                    self.y = arg
        else:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                elif key == 'width':
                    self.width = value
                elif key == 'height':
                    self.height = value
                elif key == 'x':
                    self.x = value
                elif key == 'y':
                    self.y = value

    def area(self):
        """
        "Given a Rectangle object, return the area of the rectangle."
        """
        return self.width * self.height

    def __str__(self):
        """
        The `__str__` function is a special function that is called
        when you print an object
        """
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - "\
            f"{self.width}/{self.height}"

    def display(self):
        """
        It prints a rectangle of the specified height and width.
        """
        for i in range(self.y):
                print()
        for i in range(self.height):
            for x in range(self.x):
                print(" ", end="")
            for x in range(self.width):
                print("#", end="")
            print()
        if self.height == 0:
            print()

    def to_dictionary(self):
        """
        It returns a dictionary
        representation of a Rectangle.
        """
        return {'x': self.x, 'y': self.y, 'id': self.id,
                'height': self.height, 'width': self.width}
