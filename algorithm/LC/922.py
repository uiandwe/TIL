# -*- coding: utf-8 -*-
from typing import *

class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        d1 = []
        d2 = []

        for i in A:
            if i % 2 == 0:
                d2.append(i)
            else:
                d1.append(i)
        d = []
        for i, j in zip(d2, d1):
            d.append(i)
            d.append(j)

        return d

s = Solution()
print(s.sortArrayByParityII([4, 2, 5, 7]))
