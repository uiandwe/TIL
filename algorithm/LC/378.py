# -*- coding: utf-8 -*-
import heapq

class Solution:
    def kthSmallest(self, matrix, k: int):
        h = []
        for i in matrix:
            for x in i:
                heapq.heappush(h, x)

        for i in range(k-1):
            heapq.heappop(h)

        return heapq.heappop(h)

s = Solution()
matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
]
k = 8
assert s.kthSmallest(matrix, k) == 13
