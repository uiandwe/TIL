# -*- coding: utf-8 -*-
import heapq

class Solution:
    def kClosest(self, points, K: int):
        heap = []
        for (x, y) in points:
            dist = x ** 2 + y ** 2
            heapq.heappush(heap, (dist, x, y))

        result = []
        for _ in range(K):
            (dist, x, y) = heapq.heappop(heap)
            result.append((x, y))

        return result
