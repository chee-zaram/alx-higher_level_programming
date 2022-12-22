#!/usr/bin/python3
"""Module for creating a singly linked list"""


class Node:
    """Sets/gets Node data for a singly linked list"""

    def __init__(self, data, next_node=None):
        """Initializes node info

        Args:
            data (int): Data for the node
            next_node (Node): Object of type Node representing the next node in
                the list
        """

        if not isinstance(data, int):
            raise TypeError("data must be an integer")

        self.__data = data

        if next_node and not isinstance(next_node, Node):
            raise TypeError("next_node must be a Node object")

        self.__next_node = next_node

    @property
    def data(self):
        """data getter for data method in Node class
        """
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")

        self.__data = value

    @property
    def next_node(self):
        """next_node getter"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")

        self.__next_node = value


class SinglyLinkedList(Node):
    """Creates a singly linked list"""

    def __init__(self):
        """Instantiates the private attribute head"""
        self.__head = None

    def sorted_insert(self, value):
        """Sorts the linked list and add a new node in place

        Args:
            value (int): Data to be contained in the node
        """

        newNode = Node(value)

        if self.__head is None:
            newNode.next_node = None
            self.__head = newNode
        elif self.__head.data > value:
            newNode.next_node = self.__head
            self.__head = newNode
        else:
            temp = self.__head

            while (temp.next_node and temp.next_node.data < value):
                temp = temp.next_node

            newNode.next_node = temp.next_node
            temp.next_node = newNode

    def __repr__(self):
        return "<class 'SinglyLinkedList'>"

    def __str__(self):
        """Prints the data in the list, one line per node data

        Returns:
            It returns a string of data items separated by a newline
        """

        temp = self.__head
        list_items = []

        while temp:
            list_items.append(str(temp.data))
            temp = temp.next_node

        return ('\n'.join(list_items))

    def __len__(self):
        """Gets the length of the linked list"""

        if self.__head:
            cnt = 0
            temp = self.__head

            while temp:
                cnt += 1
                temp = temp.next_node
            return cnt
        return 0
