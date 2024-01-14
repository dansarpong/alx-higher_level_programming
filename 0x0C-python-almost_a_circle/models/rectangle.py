#!usr/bin/python3
""" Module that defines the Rectangle class that inherits from Base """
from base import Base

class Rectangle(Base):
    """ Defines the Rectangle class that inherits from base """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initializes an instance of the Rectangle class """

        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """ getter for width """

        return self.__width
    
    @width.setter
    def width(self, new):
        """ setter for width """

        self.__width = new

    @property
    def height(self):
        """ getter for height """

        return self.__height
    
    @height.setter
    def height(self, new):
        """ setter for height """

        self.__height = new

    @property
    def x(self):
        """ getter for x """

        return self.__x
    
    @x.setter
    def x(self, new):
        """ setter for x """

        self.__x = new

    @property
    def y(self):
        """ getter for y """

        return self.__y
    
    @y.setter
    def y(self, new):
        """ setter for y """

        self.__y = new
