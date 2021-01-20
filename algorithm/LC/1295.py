# -*- coding: utf-8 -*-
from typing import *
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        cnt = 0
        for n in nums:
            if len(str(n)) % 2 == 0:
                cnt += 1
        return cnt



s = Solution()
assert s.findNumbers([12,345,2,6,7896]) == 2
