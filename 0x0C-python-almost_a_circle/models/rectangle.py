#!usr/bin/python3
""" Module that defines the Rectangle class that inherits from Base """
from models.base import Base


class Rectangle(Base):
    """ Defines the Rectangle class that inherits from base """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initializes an instance of the Rectangle class """

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ getter for width """

        return self.__width

    @width.setter
    def width(self, new):
        """ setter for width """

        if type(new) is not int:
            raise TypeError("width must be an integer")
        if new <= 0:
            raise ValueError("width must be > 0")

        self.__width = new

    @property
    def height(self):
        """ getter for height """

        return self.__height

    @height.setter
    def height(self, new):
        """ setter for height """

        if type(new) is not int:
            raise TypeError("height must be an integer")
        if new <= 0:
            raise ValueError("height must be > 0")

        self.__height = new

    @property
    def x(self):
        """ getter for x """

        return self.__x

    @x.setter
    def x(self, new):
        """ setter for x """

        if type(new) is not int:
            raise TypeError("x must be an integer")
        if new < 0:
            raise ValueError("x must be >= 0")

        self.__x = new

    @property
    def y(self):
        """ getter for y """

        return self.__y

    @y.setter
    def y(self, new):
        """ setter for y """

        if type(new) is not int:
            raise TypeError("y must be an integer")
        if new < 0:
            raise ValueError("y must be >= 0")

        self.__y = new

    def area(self):
        """ Function to find the area value of the rectangle instance """

        return (self.width * self.height)

    def display(self):
        """ Function to print the rectangle with # """

        print("\n" * self.y, end="")

        for i in range(self.height):
            line = (" " * self.x) + ("#" * self.width)
            print(line)

    def __str__(self):
        """ Returns a string format for the object """

        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """ Updates the attributes of the objects:
        id, width, height, x, y - respectively """

        if len(args) == 0:
            for key, value in kwargs.items():
                self.__setattr__(key, value)
            return

        try:
            self.id = args[0]
            self.width = args[1]
            self.height = args[2]
            self.x = args[3]
            self.y = args[4]
        except IndexError:
            pass

    def to_dictionary(self):
        """ Returns the dictionary representation of the instance """

        return {'x' : getattr(self, 'x'),
                'y' : getattr(self, 'y'),
                'id' : getattr(self, 'id'),
                'height' : getattr(self, "height"),
                'width' : getattr(self, "width")}
