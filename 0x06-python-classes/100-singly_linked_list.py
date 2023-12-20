#!/usr/bin/python3
""" Defines a Node and a SinglyLinkedList """


class Node:
    """ defines a class Node """

    def __init__(self, data, next_node=None):
        """ Instantiation with data and optional next_node """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """ get data attr """
        return self.__data

    @data.setter
    def data(self, value):
        """ set data attr """
        if type(value) is not int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """ get next_node attr """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """ set next node attr """
        if value is not None and type(value) is not Node:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList():
    """Defines a singly linked list"""

    def __init__(self):
        """Sets the necessary attributes for the SinglyLinkedList object."""
        self.__head = None

    def __str__(self):
        """Sets the print behavior of the SinglyLinkedList object."""
        res = ""
        node = self.__head

        if node is not None:
            while node is not None:
                res += str(node.data) + '\n'
                node = node.next_node

        return res[:-1]

    def sorted_insert(self, value):
        """ inserts node in a sorted manner """
        node = self.__head

        if node is None or self.__head.data >= value:
            self.__head = Node(value, self.__head)
        else:
            while node.next_node is not None and node.next_node.data < value:
                node = node.next_node
            node.next_node = Node(value, node.next_node)
