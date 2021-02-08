# -*- coding: utf-8 -*-
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        cur_value = root.val
        if p.val > cur_value and q.val > cur_value:
            return self.lowestCommonAncestor(root.right, p, q)

        elif p.val < cur_value and q.val < cur_value:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return root

        # d = []
        # self.min_val = min(q.val, p.val)
        # self.max_val = max(p.val, q.val)
        #
        # def search(node, depth):
        #
        #     if self.min_val <= node.val <= self.max_val:
        #         d.append((node, depth))
        #
        #     if self.min_val < node.val and node.left:
        #         search(node.left, depth + 1)
        #
        #     if self.max_val > node.val and node.right:
        #         search(node.right, depth + 1)
        #
        # search(root, 0)
        # d.sort(key=lambda x: x[1])
        # # print(d)
        # return d[0][0]



