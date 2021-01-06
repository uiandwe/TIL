# -*- coding: utf-8 -*-
from typing import *
from collections import defaultdict
class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        d = defaultdict(list)
        for i in arr:
            d[int("{0:b}".format(i).count('1'))].append(i)

        return [x for key in sorted(d.keys()) for x in sorted(d[key])]

        # return sorted(arr, key=lambda x: (bin(x).count("1"), x))

s = Solution()
assert  s.sortByBits([0,1,2,3,4,5,6,7,8]) == [0,1,2,4,8,3,5,6,7]
assert s.sortByBits([10,100,1000,10000]) == [10,100,10000,1000]
