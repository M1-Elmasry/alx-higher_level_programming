#!/usr/bin/python3
"""Represents classes to manupilating with singly linked lists"""


class Node:
    """Represents a node in a linked list.

    Attributes:
        value: The value stored in the node.
        next_node: The next node in the linked list.
    """

    def __init__(self, data, next_node=None):
        """init method of Node class
        Args:
            data (int): data of the new Node
            next_node (Node): pointer to the next Node
        """
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """getter method for data attribute"""
        return self.__data

    @data.setter
    def data(self, value):
        """setter method for data attribute

        Raises:
           TypeError: If Node is not an instance of the int class.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")

        self.__data = value

    @property
    def next_node(self):
        """getter method for next_node attribute"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """setter method for next_node attribute

        Raises:
           TypeError: If next_node is not an instance
           of the Node class or not None.
        """
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")

        self.__next_node = value


class SinglyLinkedList:
    """represents a singly linked list

    attributes:
        head (Node or None): head of the linked list
    """

    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        """method to insert a new Node into
        the correct sorted position in the list (increasing order)

        Args:
            value (int): the value of the new Node
        """
        new_node = Node(value)

        if self.__head is None:
            self.__head = new_node
            return

        # handle if the new node is the least
        if value < self.__head.data:
            new_node.next_node = self.__head.next_node
            self.__head = new_node
            return

        curr = self.__head

        while curr.next_node is not None and curr.next_node.data <= value:
            curr = curr.next_node

        new_node.next_node = curr.next_node
        curr.next_node = new_node

    def __str__(self):
        """printing the list Nodes data"""
        nums = []
        curr = self.__head
        while curr is not None:
            nums.append(str(curr.data))
            curr = curr.next_node

        return "\n".join(nums)
