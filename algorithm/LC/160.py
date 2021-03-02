# -*- coding: utf-8 -*-
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from collections import defaultdict
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        d = defaultdict(object)
        while headA:
            d[headA] = headA.val
            headA = headA.next

        while headB:
            if headB in d.keys():
                return headB
            headB = headB.next
