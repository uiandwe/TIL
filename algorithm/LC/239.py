# -*- coding: utf-8 -*-
import collections

class Solution:
    def maxSlidingWindow(self, nums, k: int):
        deque = collections.deque()
        res = []
        for i, num in enumerate(nums):
            while (deque and nums[deque[-1]] < num):
                deque.pop()
            if (deque and i - deque[0] >= k):
                deque.popleft()
            deque.append(i)
            res.append(nums[deque[0]])
            print(deque, res)
        return res[k - 1:]
