# -*- coding: utf-8 -*-
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        #         def reverse(node, end=None):
        #             if not node:
        #                 return end

        #             next, node.next = node.next, end
        #             return reverse(next, node)

        #         return reverse(head)
        node, prev = head, None

        while node:
            next, node.next = node.next, prev
            prev, node = node, next

        return prev
