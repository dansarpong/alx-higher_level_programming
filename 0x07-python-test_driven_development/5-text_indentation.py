#!/usr/bin/python3
""" Defines a text_indentation function that prints a text with 2 new lines after each of these characters: ., ? and : """


def text_indentation(text):
    """ Prints a text with 2 new lines after each of these characters: ., ? and : """
    if type(text) is not str:
        raise TypeError("text must be a string")
    else:
        text = text.replace(". ", ".\n\n")
        text = text.replace("? ", "?\n\n")
        text = text.replace(": ", ":\n\n")
        print(text, end="")
