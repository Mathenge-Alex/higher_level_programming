#!/usr/bin/python3
"""Define classes for a singly-linked list."""


class Node:
    """Representing a node in a singly-linked list."""

    def __init__(self, data, next_node=None):
        """Initializing a new Node.
        Args:
            data (int): The data of the new Node.
            next_node (Node): The next node of the new Node.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Get/set the data of the Node."""
        return (self.__data)

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Get/set the next_node of the Node."""
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Representing a singly-linked list."""

    def __init__(self):
        """Initalizing a new SinglyLinkedList."""
        self.__head = None

    def sorted_insert(self, value):
        """Inserting a new Node to the SinglyLinkedList.
        The node is inserted at the correct ordered numerical position.
        Args:
            value (Node): The new Node to insert.
        """
        new_nd = Node(value)
        if self.__head is None:
            new_nd.next_node = None
            self.__head = new_nd
        elif self.__head.data > value:
            new_nd.next_node = self.__head
            self.__head = new_nd
        else:
            tmp = self.__head
            while (tmp.next_node is not None and
                    tmp.next_node.data < value):
                tmp = tmp.next_node
            new_nd.next_node = tmp.next_node
            tmp.next_node = new_nd

    def __str__(self):
        """Defining the print() representation of a SinglyLinkedList."""
        vals = []
        tmp = self.__head
        while tmp is not None:
            vals.append(str(tmp.data))
            tmp = tmp.next_node
        return ('\n'.join(vals))
