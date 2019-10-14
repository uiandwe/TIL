# -*- coding: utf-8 -*-
class Heap:
    def __init__(self):
        self.arr = []

    def reheap_down(self, idx):

        if (idx*2) + 1 < len(self.arr):
            right = 0
            left = self.arr[idx*2+1]

            if idx * 2 + 2 < len(self.arr) - 1:
                right = self.arr[idx * 2 + 2]
            if left > right:
                large = idx * 2 + 1
            else:
                large = idx * 2 + 2

            if self.arr[idx] < self.arr[large]:
                self.arr[idx], self.arr[large] = self.arr[large], self.arr[idx]
                self.reheap_down(large)

    def reheap_up(self, idx):
        if idx:
            parent = (idx - 1) // 2
            if self.arr[idx] > self.arr[parent]:
                self.arr[idx], self.arr[parent] = self.arr[parent], self.arr[idx]
                self.reheap_up(parent)

    def insert(self, number):
        self.arr.append(number)
        self.reheap_up(len(self.arr)-1)
        return True

    def delete(self):
        if len(self.arr) <= 0:
            return False

        del_number = self.arr.pop(0)
        self.reheap_down(0)
        return del_number

    def sort(self):
        return [self.delete() for x in range(len(self.arr))]





h = Heap()
h.insert(1)
h.insert(3)
h.insert(2)

print(h.arr)

print(h.sort())

h.insert(1)
h.insert(3)
h.insert(2)

print(h.delete())
print(h.delete())
print(h.delete())

