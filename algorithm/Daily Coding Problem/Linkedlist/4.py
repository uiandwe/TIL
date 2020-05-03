# -*- coding: utf-8 -*-
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Solution:
    def insert(self,head,data):
            p = Node(data)
            if head==None:
                head=p
            elif head.next==None:
                head.next=p
            else:
                start=head
                while(start.next!=None):
                    start=start.next
                start.next=p
            return head
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def removeDuplicates(self,head):
        before_node = None
        answer = []
        while head:
            if before_node:
                now_data = head.data
                if now_data == before_node.data:
                    before_node.next = head.next
                else:
                    answer.append(before_node.data)
            before_node = head
            head = head.next
        answer.append(before_node.data)
        print(" ".join(map(str, answer)))

mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)
head=mylist.removeDuplicates(head)
mylist.display(head)
