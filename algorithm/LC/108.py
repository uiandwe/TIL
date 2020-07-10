# -*- coding: utf-8 -*-
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def helper(self, nums, start, end):
        if start > end:
            return None

        mid = (start + end) // 2
        node = TreeNode(nums[mid])
        node.left = self.helper(nums, start, mid - 1)
        node.right = self.helper(nums, mid + 1, end)
        return node

    def sortedArrayToBST(self, nums):
        if not nums:
            return None

        if len(nums) <= 0:
            return []

        return self.helper(nums, 0, len(nums) - 1)



temp = [0, 1, 2, 3, 4, 5]

print(len(temp)//2, temp[len(temp)//2])
