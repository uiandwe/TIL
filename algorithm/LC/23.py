# -*- coding: utf-8 -*-
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


from queue import PriorityQueue
from typing import *


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        q = PriorityQueue()

        curr = head = ListNode()

        for n in lists:
            while n:
                q.put(n.val)
                n = n.next

        ret = ListNode()
        head = ret
        while not q.empty():
            ret.next = ListNode(q.get())
            ret = ret.next

        return head.next
