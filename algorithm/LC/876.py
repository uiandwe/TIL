# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        r = t = head

        while r:
            r = r.next
            if r:
                r = r.next
                t = t.next

        return t
