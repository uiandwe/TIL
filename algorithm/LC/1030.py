# -*- coding: utf-8 -*-
from typing import *
class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:

        d = []
        for i in range(R):
            for j in range(C):
                d.append([i,j])

        def key(x):
            return abs(x[0]-r0)+abs(x[1]-c0)

        d.sort(key=key)
        return d

s = Solution()
assert s.allCellsDistOrder(R = 1, C = 2, r0 = 0, c0 = 0) == [[0,0],[0,1]]
