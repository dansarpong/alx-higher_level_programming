#!/usr/bin/python3
""" Defines a class BaseGeometry """


class BaseGeometry:
    """ A class based on geometry shapes """

    def area(self):
        """ Raises an Exception with a message """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Validates a value """

        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
