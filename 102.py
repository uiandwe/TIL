# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        d = deque([root])

        ret = []

        while d:
            temp = []
            for _ in range(len(d)):
                node = d.popleft()
                if node:
                    temp.append(node.val)
                    if node.left:
                        d.append(node.left)
                    if node.right:
                        d.append(node.right)
            ret.append(temp)
        return ret


