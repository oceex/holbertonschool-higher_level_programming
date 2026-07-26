#!/usr/bin/python3
"""

Singly Linked List

"""


class Node:
    "  the node class "
    def __init__(self, data, next_node=None):
        " intialsing the node "
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        " return the data it hold "
        return self.__data

    @property
    def next_node(self):
        " return the link that it hold "
        return self.__next_node

    @data.setter
    def data(self, val):
        " set the data it hold "
        if not isinstance(val, int):
            raise TypeError("data must be an integer")
        self.__data = val

    @next_node.setter
    def next_node(self, val):
        " set the link that it hold "
        if not (isinstance(val, Node) or val is None):
            raise TypeError("next_node must be a Node object")
        self.__next_node = val


class SinglyLinkedList:
    " the array's class "
    def __init__(self):
        " intialise the array "
        self.__head = None
        self.__list = []

    def __str__(self):
        " to print all the data "
        m = ""
        for n in self.__list:
            m += str(n.data) + '\n'
        return m

    def sorted_insert(self, value):
        " to insert the data in the sorted order "
        self.__list.append(Node(value, self.__head))
        self.__list = sorted(self.__list, key=lambda x: x.data)
        head = self.__list[len(self.__list) - 1]
