# -*- coding: utf-8 -*-
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        #         head = ListNode()
        #         pre = head

        #         while p1 and p2:
        #             if p1.val <= p2.val:
        #                 pre.next = p1
        #                 p1 = p1.next
        #             else:
        #                 pre.next = p2
        #                 p2 = p2.next
        #             pre = pre.next
        #         if p1:
        #             pre.next = p1
        #         else:
        #             pre.next = p2
        #         return head.next

        if (not l1) or (l2 and l1.val > l2.val):
            l1, l2 = l2, l1
        if l1:
            l1.next = self.mergeTwoLists(l1.next, l2)
        return l1
