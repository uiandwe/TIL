# -*- coding: utf-8 -*-
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:

        from collections import deque

        if not root:
            return True
        if not root.left and not root.right:
            return True
        if not root.left or not root.right:
            return False

        q_l, q_r = deque([root.left]), deque([root.right])

        while q_l and q_r:
            left_node, right_node = q_l.popleft(), q_r.popleft()

            if not left_node and not right_node:
                continue

            if not left_node or not right_node:
                return False

            if left_node.val != right_node.val:
                return False

            q_l.append(left_node.left)
            q_l.append(left_node.right)

            q_r.append(right_node.right)
            q_r.append(right_node.left)

        if not q_l and not q_r:
            return True
        else:
            return False





