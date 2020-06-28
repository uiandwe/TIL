# -*- coding: utf-8 -*-
from queue import Queue

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    init = False
    prev = 0
    min_value = float('inf')

    def getMinimumDifference(self, root: TreeNode) -> int:
        q = Queue()
        q.put(root)
        self.inOrder(root)

        return self.min_value

    def inOrder(self, node):
        if not node:
            return
        self.inOrder(node.left)

        if not self.init:
            self.init = True
        else:
            self.min_value = min(self.min_value, abs(node.val-self.prev))

        self.prev = node.val

        self.inOrder(node.right)



s = Solution()
leaf = TreeNode(2)
middle = TreeNode(3, left=leaf)
tree = TreeNode(1, right=middle)

assert 1 == s.getMinimumDifference(tree)
