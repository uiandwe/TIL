# [::-1] 보다 reverse()가 더 빠르다 (훠월씬)
# https://leetcode.com/problems/palindrome-linked-list/submissions/


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
        
        c = d.copy()
        d.reverse()
        
        return c == d
