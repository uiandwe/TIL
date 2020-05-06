# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque


class Solution:
    def maxDepth(self, root) -> int:
        if root is None:
            return 0

        q = deque()
        q.append((root, 1))
        depth = 1

        while q:
            node, temp_depth = q.popleft()
            depth = max(depth, temp_depth)
            if node and node.left:
                q.append((node.left, temp_depth + 1))

            if node and node.right:
                q.append((node.right, temp_depth + 1))

        return depth
