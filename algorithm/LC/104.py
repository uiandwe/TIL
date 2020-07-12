# -*- coding: utf-8 -*-
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque


class Solution:
    def maxDepth(self, root) -> int:
        if not root:
            return 0

        q = deque()
        q.append((root, 1))
        depth = 1

        while q:
            node, node_depth = q.popleft()
            depth = max(depth, node_depth)

            if node.left:
                q.append((node.left, node_depth + 1))

            if node.right:
                q.append((node.right, node_depth + 1))

        return depth
