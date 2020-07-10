# -*- coding: utf-8 -*-
class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def preorder(root):
    if root is None:
        return
    print("node : ", root.value)
    if root.left:
        preorder(root.left)
    if root.right:
        preorder(root.right)






right1 = Node(3)
left1 = Node(2)
root = Node(1, left1, right1)

if __name__ == '__main__':
    preorder(root)
