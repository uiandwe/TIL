# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        t = r = ListNode(next=head)

        index = 0
        while index < n:
            t = t.next
            index += 1

        while t and t.next:
            t = t.next
            r = r.next

        if r.next:
            temp = r.next

            if temp and temp.next:
                r.next = temp.next
            else:
                r.next = None

            if temp == head:
                head = head.next

        return head
