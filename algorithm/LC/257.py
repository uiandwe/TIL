# -*- coding: utf-8 -*-
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorder(self, node, s, array):
        if not node:
            return

        if not node.left and not node.right:
            s += "{}".format(node.val)
            array.append(s)
        else:
            s += "{}{}".format(node.val, "->")

        if node.left:
            self.preorder(node.left, s, array)

        if node.right:
            self.preorder(node.right, s, array)

    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        s = ""
        array = []
        self.preorder(root, s, array)
        return array

