#!/usr/bin/python3
"""
Rectangle module.
This module contains a class that defines a Rectangle.
"""


class Rectangle:
    """
    class that create a rectangle
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        set the size of the rectangle
        """
        self.__width = width
        self.__height = height
        type(self).number_of_instances += 1
        type(self).print_symbol

    @property
    def width(self):
        """
        return the width value
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        set the width value
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        return the height value
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        set the height value
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """
        return the area of a rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        calculate the perimeter of a rectangle
        """
        perimeter = 0
        if self.__height == 0 or self.__width == 0:
            perimeter = 0
        else:
            perimeter = self.__width * 2 + self.__height * 2
        return perimeter

    def __str__(self):
        """
        function that print a rectangle
        """
        rectangle = ""
        if self.__width == 0 or self.__height == 0:
            return rectangle
        for i in range(self.__height):
            for j in range(self.__width):
                rectangle += str(self.print_symbol)
            if i < self.__height - 1:
                rectangle += "\n"
        return rectangle

    def __repr__(self):
        """
        return the line commands that can create a new instance
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """
        when the instance get deleted this methods is called
        """
        print("Bye rectangle...")
        type(self).number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        function that return the biggest rectangle
        if its equal it returns rect_1
        if a rectangle is not an instance of the rectangle class
        it raise a type error
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        area_1 = rect_1.area()
        area_2 = rect_2.area()

        if area_1 > area_2:
            return rect_1
        elif area_1 < area_2:
            return rect_2
        else:
            return rect_1

    @classmethod
    def square(cls, size=0):
        """
        class method that create a square instead of a rectangle
        """
        Rectangle.__height = size
        Rectangle.__width = size
        return cls()
