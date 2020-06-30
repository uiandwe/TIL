# -*- coding: utf-8 -*-
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: TreeNode):
        ret = []
        self.travers(root, ret)
        return ret

    def travers(self, node, ret):
        if node:
            if node.left:
                self.travers(node.left, ret)

            ret.append(node.val)

            if node.right:
                self.travers(node.right, ret)


left = TreeNode(3)
right = TreeNode(2, left=left)
root = TreeNode(1, right=right)

s = Solution()
s.inorderTraversal(root)
