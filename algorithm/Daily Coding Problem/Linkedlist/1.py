# -*- coding: utf-8 -*-
"""

Given the head of a singly linked list, reverse it in-place.

"""


class Node:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        node = self
        string = ""
        while node:
            string += "{} ->".format(node.val)
            node = node.next

        return string


def set_nodes(values):
    next_node = None
    for value in values[::-1]:
        node = Node(value)
        node.next = next_node
        next_node = node

    return next_node


def get_list(head):
    node = head
    nodes = list()
    while node:
        nodes.append(node.val)
        node = node.next

    return nodes


def reverse_list(head, new_head):
    if not head:
        return new_head

    old_head = head.next
    head.next = new_head

    return reverse_list(old_head, head)

print(get_list(set_nodes([1, 2])))
print(reverse_list(set_nodes([1, 2]), None))
