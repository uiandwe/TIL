# -*- coding: utf-8 -*-
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head) -> bool:
        d = []

        while head:
            d.append(head.val)
            head = head.next
        print(d, d[::-1])
        return d == d[:-1]


s = Solution()
print(s.isPalindrome(1))
