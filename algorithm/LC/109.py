# -*- coding: utf-8 -*-
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import *
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        nums = []
        while head:
            nums.append(head.val)
            head = head.next

        def sortedArrayToBST(arr):
            if not arr:
                return None

            mid = len(arr) // 2

            node = TreeNode(arr[mid])
            node.left = sortedArrayToBST(arr[:mid])
            node.right = sortedArrayToBST(arr[mid + 1:])
            return node

        root = sortedArrayToBST(nums)
        print(root)
        return root
