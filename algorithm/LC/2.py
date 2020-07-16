# -*- coding: utf-8 -*-
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        d = []
        while l1 and l2:
            d.append(l1.val + l2.val)

            l1 = l1.next
            l2 = l2.next

        while l1:
            d.append(l1.val)
            l1 = l1.next

        while l2:
            d.append(l2.val)
            l2 = l2.next

        root = result = None
        round_up = 0
        for i in range(len(d)):
            if i == 0:
                root = result = ListNode((d[i] + round_up) % 10)
            else:
                result.next = ListNode((d[i] + round_up) % 10)
                result = result.next

            if d[i] + round_up > 9:
                round_up = 1
            else:
                round_up = 0

        if round_up == 1:
            result.next = ListNode(1)

        return root
