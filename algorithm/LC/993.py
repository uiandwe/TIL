# -*- coding: utf-8 -*-
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        from collections import deque

        q = deque()
        q.append((0, root, None))

        x_depth = -1
        y_depth = -1
        x_parent = None
        u_parent = None

        while q:
            node = q.popleft()
            # print(node[0], node[1].val)
            if node[1].val == x:
                x_depth = node[0]
                x_parent = node[2]
                # print(x_depth, x_parent.val)

            if node[1].val == y:
                y_depth = node[0]
                y_parent = node[2]
                # print(y_depth, y_parent.val)

            if node[1].left:
                q.append((node[0] + 1, node[1].left, node[1]))

            if node[1].right:
                q.append((node[0] + 1, node[1].right, node[1]))

        if x_depth == y_depth and x_parent != y_parent:
            return True

        return False
