# -*- coding: utf-8 -*-
"""

Implement a queue using two stacks.

Recall that a queue is a FIFO (first-in, first-out) data structure with the following methods: enqueue,

which inserts an element into the queue, and dequeue, which removes it.

"""


class Stack:
    __slots__ = ('array')

    def __init__(self):
        self.array = []

    def push(self, value: int):
        self.array.append(value)

    def pop(self)-> int:
        if self.empty() is False:
            return self.array.pop()
        else:
            return -1

    def size(self):
        return len(self.array)

    def empty(self):
        if len(self.array) > 0:
            return False
        else:
            return True


class Queue:
    __slots__ = ('stack1', 'stack2')

    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def enqueue(self, value: int):
        self.stack1.push(value)

    def dequeue(self) -> int:
        if self.stack2.empty() is True and self.stack1.empty() is True:
            return -1

        if self.stack2.empty() is True:
            while self.stack1.empty() is False:
                self.stack2.push(self.stack1.pop())

        return self.stack2.pop()


if __name__ == '__main__':
    q = Queue()
    q.enqueue(1)
    assert q.dequeue() == 1
    assert q.dequeue() == -1
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    assert q.dequeue() == 2
    assert q.dequeue() == 3
    assert q.dequeue() == 4
    assert q.dequeue() == -1
