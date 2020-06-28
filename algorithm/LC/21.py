# -*- coding: utf-8 -*-
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    root = None
    tail = None

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        lh = l1
        rh = l2
        while lh and rh:
            if lh.val <= rh.val:
                self.addNode(lh)
                lh = lh.next
            else:
                self.addNode(rh)
                rh = rh.next

        while lh:
            self.addNode(lh)
            lh = lh.next

        while rh:
            self.addNode(rh)
            rh = rh.next

        return self.root

    def addNode(self, node):
        if not self.root:
            self.root = ListNode(node.val)
            self.tail = self.root
        else:
            self.tail.next = ListNode(node.val)
            self.tail = self.tail.next

s = Solution()
ln = ListNode(1, ListNode(2, ListNode(4)))
rn = ListNode(1, ListNode(3, ListNode(4)))
s.mergeTwoLists(ln, rn)
