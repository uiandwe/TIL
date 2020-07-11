# -*- coding: utf-8 -*-
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        if not root:
            return

        arr = []
        self.inorder(root, arr)

        # print(arr)

        from collections import deque

        q = deque()
        q.append(root)

        while q:
            node = q.popleft()
            index = arr.index(node.val)
            node.val = sum(arr[index + 1:]) + node.val

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        return root

    def inorder(self, node, arr):
        if not node:
            return

        if node.left:
            self.inorder(node.left, arr)

        arr.append(node.val)

        if node.right:
            self.inorder(node.right, arr)
