# -*- coding: utf-8 -*-
from collections import deque

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def getHeight(self,root):
        q = deque()
        q.append((root, 0))
        max_depth = 0
        while q:
            node, depth = q.popleft()
            max_depth = max(depth, max_depth)

            if node.left:
                q.append((node.left, depth + 1))
            if node.right:
                q.append((node.right, depth +1))

        return max_depth

T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
height=myTree.getHeight(root)
print(height)
