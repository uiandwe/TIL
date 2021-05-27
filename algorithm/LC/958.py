# -*- coding: utf-8 -*-
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict


class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:

        q = deque()
        q.append(root)

        while q:
            node = q.popleft()
            if not node and q:
                return not any(q)
            elif node:
                q.append(node.left)
                q.append(node.right)

        return True
