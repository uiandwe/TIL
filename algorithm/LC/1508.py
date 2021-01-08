# -*- coding: utf-8 -*-
from typing import *
from itertools import accumulate

class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        ret = []
        for i in range(n):
            val = nums[i]
            ret.append(val)
            for j in range(i+1, n):
                val += nums[j]
                ret.append(val)

        ret.sort()
        return sum(ret[left-1: right]) % (10**9 + 7)



s = Solution()
assert s.rangeSum([1,2,3,4], n = 4, left = 1, right = 5) == 13
assert s.rangeSum(nums = [1,2,3,4], n = 4, left = 3, right = 4) == 6
assert s.rangeSum(nums = [1,2,3,4], n = 4, left = 1, right = 10) == 50
