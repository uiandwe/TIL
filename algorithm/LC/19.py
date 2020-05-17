# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        
        sentinel = ListNode(-1)
        sentinel.next = head
        s = f = sentinel
        
        i = 0
        
        while f and i <= n:
            f = f.next
            i += 1
        
        while f:
            f = f.next
            s = s.next
        
        s.next = s.next.next            
        return sentinel.next
            
            
        
        
        
