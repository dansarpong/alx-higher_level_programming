#!/usr/bin/python3
""" Module that defines the class Student
"""


class Student:
    """ Class to create student instances """

    def __init__(self, first_name, last_name, age):
        """ Special method to initialize """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attr=None):
        """ Method that returns directory description """

        ans = self.__dict__.copy()

        if type(attr) is list:
            res = {}

            for item in attr:
                if type(item) is not str:
                    return ans
                if item in ans.keys():
                    res[item] = ans[item]

            return res

        return ans

    def reload_from_json(self, json):
        """ Replaces all attributes of the Student instance """

        for atr in json:
            self.__dict__[atr] = json[atr]
