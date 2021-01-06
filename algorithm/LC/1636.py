# -*- coding: utf-8 -*-

from typing import *
from collections import Counter, defaultdict
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        c = Counter(nums)

        def d(x):
            return c[x]

        nums.sort(reverse=True)
        nums.sort(key=d)

        return nums

s = Solution()
s.frequencySort([2,3,1,3,2])

