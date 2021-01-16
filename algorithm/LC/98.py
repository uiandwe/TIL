# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        d = []
        self.ret = True

        def dfs(node):
            if node:
                if node.left:
                    dfs(node.left)
                if len(d) > 0 and d[-1] >= node.val:
                    self.ret = False

                d.append(node.val)

                if node.right:
                    dfs(node.right)

        dfs(root)

        return self.ret
