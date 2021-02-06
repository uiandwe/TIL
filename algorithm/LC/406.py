# -*- coding: utf-8 -*-
from typing import *
import heapq

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        d = []
        for p in people:
            heapq.heappush(d, (-p[0], p[1]))

        ret = []
        while d:
            item = heapq.heappop(d)
            ret.insert(item[1], [-item[0], item[1]])

        return ret




s = Solution()
s.reconstructQueue([[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]) == [[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
