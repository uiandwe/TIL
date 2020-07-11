# -*- coding: utf-8 -*-
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:
            return 0

        from collections import deque
        result = 0
        q = deque()
        q.append(('r', root))

        while q:
            node = q.popleft()
            # print(node[0], node[1])
            if node[0] == 'l' and not node[1].left and not node[1].right:
                result += node[1].val

            if node[1].left:
                q.append(('l', node[1].left))

            if node[1].right:
                q.append(('r', node[1].right))

        return result

