#!/usr/bin/python3
""" Module that defines the Square class that inherits from Rectangle """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Defines the Square class that inherits from Rectangle """

    def __init__(self, size, x=0, y=0, id=None):
        """ Initializes an instance of the Square class """

        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ Returns a string format for the object """

        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """ Getter for size attribute """

        return self.width

    @size.setter
    def size(self, new):
        """ Setter for size attribute """

        self.width = new
        self.height = new

    def update(self, *args, **kwargs):
        """ Updates the attributes of the object:
        id, size, x, y - respectively """

        if len(args) == 0:
            for key, value in kwargs.items():
                self.__setattr__(key, value)
            return

        try:
            self.id = args[0]
            self.size = args[1]
            self.x = args[2]
            self.y = args[3]
        except IndexError:
            pass

    def to_dictionary(self):
        """ Returns the dictionary representation of the instance """

        ref = super().to_dictionary()
        ref.pop("width")
        ref["size"] = ref.pop("height")
        return ref
