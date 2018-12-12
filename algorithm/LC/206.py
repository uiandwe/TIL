class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def printList(self, head):
        while head is not None:
            print(head.val)
            head = head.next

    def reverseList(self, head):
        new_head = None
        while head:
            p = head
            head = head.next
            p.next = new_head
            new_head = p

        return new_head

s = Solution()
root = ln = None

for i in range(5):
    temp_ln = ListNode(i)
    if root is None:
        root = ln = temp_ln
    else:
        while ln.next is not None:
            ln = ln.next
        ln.next = temp_ln

s.printList(root)

root = s.reverseList(root)

s.printList(root)
