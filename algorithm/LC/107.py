# -*- coding: utf-8 -*-
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


import queue

class Solution:

    def levelOrderBottom(self, root):
        ret = []

        q = queue.Queue()
        q.put(root)

        while not q.empty():
            temp = []
            for i in range(q.qsize()):
                node = q.get()
                if node:
                    temp.append(node.val)
                    if node.left:
                        q.put(node.left)
                    if node.right:
                        q.put(node.right)

            ret.append(temp)

        return reversed(ret)







right2 = TreeNode(7)
left2 = TreeNode(15)
right1 = TreeNode(20, left2, right2)
left1 = TreeNode(9)
root = TreeNode(3, left1, right1)


s = Solution()
s.levelOrderBottom(root)
