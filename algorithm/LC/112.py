# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        
        d = []
        dq = deque()
        dq.append((root, 0))
        
        while dq:
            node, s = dq.popleft()
            if node:
                
                if node.left:
                    dq.append((node.left, node.val+s))
                if node.right:
                    dq.append((node.right, node.val+s))
                
                if node.right is None and node.left is None:
                    d.append(node.val+s)
                    
        return sum in d
        
