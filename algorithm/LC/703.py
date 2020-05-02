# -*- coding: utf-8 -*-
import heapq


class KthLargest:

    def __init__(self, k: int, nums):
        self.k = k
        self.q = nums

    def add(self, val: int) -> int:
        self.q.append(val)
        self.q.sort()
        return self.q[self.k*-1]

# Your KthLargest object will be instantiated and called as such:
obj = KthLargest(3, [4, 5, 8, 2])
param_1 = obj.add(3)
param_1 = obj.add(5)
