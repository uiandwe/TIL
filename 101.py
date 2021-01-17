# -*- coding: utf-8 -*-
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:

        d = deque([root])

        while d:
            temp = [n.val if n else None for n in d]
            # print(temp)
            if temp != temp[::-1]:
                return False

            for _ in range(len(d)):
                node = d.popleft()
                if node:
                    d.append(node.left)
                    d.append(node.right)

        return True





