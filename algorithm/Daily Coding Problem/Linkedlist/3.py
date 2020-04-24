# -*- coding: utf-8 -*-
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Solution:

    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def insert(self,head,data):
        n = Node(data)
        current = head

        if current is None:
            head = n
            return head

        while current.next:
            current = current.next

        current.next = n

        return head

mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)
mylist.display(head)
