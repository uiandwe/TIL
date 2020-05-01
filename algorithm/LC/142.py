# -*- coding: utf-8 -*-
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def detectCycle(self, head):
        t = r = head
        if r is None:
            return "no cycle"

        while True:
            r = r.next
            if r is None:
                return "no cycle"

            t = t.next
            r = r.next

            if r is None:
                return "no cycle"

            if t == r:
                break

        r = head
        index = 0
        while t != r:
            r = r.next
            t = t.next
            index += 1
        return "tail connects to node index "+str(index)
