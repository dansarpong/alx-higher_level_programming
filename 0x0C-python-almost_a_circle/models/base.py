#!/usr/bin/python3
""" This module defines the Base class for the project """
import json
import csv
import turtle
import time


class Base:
    """ The Base class for the project """

    __nb_objects = 0

    def __init__(self, id=None):
        """ The initializing function for the Base class """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Returns the JSON string representation of list_dictionaries """

        if list_dictionaries is not None and list_dictionaries != []:
            return json.dumps(list_dictionaries)
        return "[]"

    @classmethod
    def save_to_file(cls, list_objs):
        """ Writes the JSON string representation of list_objs to a file """

        file = cls.__name__ + ".json"
        with open(file, "w") as f:
            if list_objs is None:
                f.write("[]")
            else:
                list_dicts = [obj.to_dictionary() for obj in list_objs]
                f.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """ Returns the list of the JSON string representation json_string """

        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ Returns an instance with all atributes already set """

        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return new

    @classmethod
    def load_from_file(cls):
        """ Returns a list of instances """

        file = cls.__name__ + ".json"
        try:
            with open(file, "r") as f:
                list_dict = Base.from_json_string(f.read())
                return [cls.create(**d) for d in list_dict]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ Serializes in CSV to csv file """

        file = cls.__name__ + ".csv"
        with open(file, 'w', newline='') as f:
            if list_objs is None or list_objs == []:
                f.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = [obj.to_dictionary() for obj in list_objs]
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writerows(list_dicts)

    @classmethod
    def load_from_file_csv(cls):
        """ Deserializes a csv file and return list of instances """

        file = cls.__name__ + ".csv"
        try:
            with open(file, newline='') as f:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                reader = csv.DictReader(f, fieldnames=fieldnames)
                list_dicts = []
                for row in reader:
                    list_dicts += [dict((i, int(j)) for i, j in row.items())]
                return [cls.create(**obj) for obj in list_dicts]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """ Opens a window and draws all the Rectangles and Squares """

        turtle.setup(width=.35, height=.5, startx=0, starty=0)
        turtle.title("Rectangle and Squares drawing")
        turtle.delay(15)
        t = turtle.Turtle()
        t.hideturtle()

        if list_rectangles is not None and list_rectangles != []:
            t.color("red", "yellow")
            for obj in list_rectangles:
                t.up()
                t.home()
                t.goto(obj.x, obj.y)
                t.begin_fill()
                t.down()
                for i in range(2):
                    t.forward(obj.width)
                    t.right(90)
                    t.forward(obj.height)
                    t.right(90)
                t.end_fill()

        time.sleep(1.5)

        if list_squares is not None and list_squares != []:
            t.color("green", "blue")
            for obj in list_squares:
                t.up()
                t.home()
                t.goto(obj.x, obj.y)
                t.begin_fill()
                t.down()
                for i in range(2):
                    t.forward(obj.width)
                    t.right(90)
                    t.forward(obj.height)
                    t.right(90)
                t.end_fill()

        time.sleep(3)
        turtle.bye()
