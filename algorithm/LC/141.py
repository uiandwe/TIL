# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def hasCycle(self, head):
        t = r = head
        if r is None:
            return False

        while True:
            r = r.next
            if r is None:
                return False

            t = t.next
            r = r.next

            if r is None:
                return False

            if t == r:
                break

        return True
