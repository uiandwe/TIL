# -*- coding: utf-8 -*-
import heapq


class Solution:
    def findKthLargest(self, nums, k):
        h = []
        for i in nums:
            heapq.heappush(h, i*-1)

        for i in range(k-1):
            heapq.heappop(h)
        return heapq.heappop(h)*-1


s = Solution()
assert s.findKthLargest([3,2,1,5,6,4], 2) == 5
s.findKthLargest([3,2,3,1,2,4,5,5,6], 4)
s.findKthLargest([1], 1)
s.findKthLargest([99, 99], 2)
