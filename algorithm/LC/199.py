# -*- coding: utf-8 -*-
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:

        d = defaultdict(list)
        result = []

        def dfs(node, depth):
            if node:
                d[depth].append(node.val)
                if node.left:
                    dfs(node.left, depth + 1)
                if node.right:
                    dfs(node.right, depth + 1)

        dfs(root, 0)

        for k in d.keys():
            result.append(d[k][-1])

        # print(result)
        return result
