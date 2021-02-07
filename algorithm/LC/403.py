# -*- coding: utf-8 -*-
from typing import *
class Solution:
    def canCross(self, stones: List[int]) -> bool:
        d = [set() for _ in range(len(stones))]

        d[0].add(1)

        for i in range(1, len(stones)):
            for j in range(i):
                diff = stones[i] - stones[j]

                if diff in d[j]:
                    d[i].add(diff-1)
                    d[i].add(diff)
                    d[i].add(diff+1)

        return True if len(d[-1]) > 0 else False



s = Solution()
assert s.canCross([0,1,3,5,6,8,12,17]) is True
assert s.canCross([0,1,2,3,4,8,9,11]) is False
