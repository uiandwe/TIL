# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = temp = None
        while head:
            prev = head
            head = head.next
            prev.next = temp
            temp = prev
            
        return prev
       
        
