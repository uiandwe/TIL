# -*- coding: utf-8 -*-
from typing import *
import heapq
from collections import Counter

class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        c = Counter(barcodes)
        d = []
        for key, value in c.items():
            heapq.heappush(d, (-value, key))

        result = []
        while len(d) > 1:
            x = heapq.heappop(d)
            y = heapq.heappop(d)

            result.append(x[1])
            result.append(y[1])

            if x[0] + 1 < 0:
                heapq.heappush(d, (x[0]+1, x[1]))
            if y[0] + 1 < 0:
                heapq.heappush(d, (y[0] + 1, y[1]))

        if d:
            result.append(d[0][1])
        return result

s = Solution()
# assert s.rearrangeBarcodes([1,1,1,1,2,2,3,3]) == [1,3,1,3,1,2,1,2]
# assert s.rearrangeBarcodes([1,1,1,2,2,2]) == [2,1,2,1,2,1]
assert s.rearrangeBarcodes([2,2,1,3]) == [2, 1, 2, 3]

