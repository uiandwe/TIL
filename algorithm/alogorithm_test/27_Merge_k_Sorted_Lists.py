# -*- coding: utf-8 -*-
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from queue import PriorityQueue


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        q = PriorityQueue()

        for l in lists:
            while l:
                q.put(l.val)
                l = l.next

        ret = ListNode()
        head = ret
        while not q.empty():
            ret.next = ListNode(q.get())
            ret = ret.next

        return head.next
