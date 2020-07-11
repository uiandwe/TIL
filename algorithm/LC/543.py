# -*- coding: utf-8 -*-
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.result = 0

        def depth(node):
            if not node:
                return 0

            left_node = depth(node.left)
            right_node = depth(node.right)
            self.result = max(self.result, left_node + right_node)
            return max(left_node, right_node) + 1

        depth(root)
        return self.result


