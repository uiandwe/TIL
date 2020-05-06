# -*- coding: utf-8 -*-
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        q = deque()
        q.append(root)

        while q:
            node = q.popleft()

            if node:
                node.left, node.right = node.right, node.left

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

        return root
