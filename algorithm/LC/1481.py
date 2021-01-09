# -*- coding: utf-8 -*-
from typing import *
from collections import Counter, defaultdict
class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        di = Counter(arr)

        d = defaultdict(list)
        for num, freq in di.items():
            d[freq].append(num)

        array = sorted(d.keys())

        for key in array:
            while d[key] and k > 0:
                k -= key
                if k >= 0:
                    del di[d[key].pop()]

        ret = 0
        for key in d.keys():
            ret += len(d[key])
        return ret



s = Solution()
assert s.findLeastNumOfUniqueInts([4,3,1,1,3,3,2], k = 3) == 2
assert s.findLeastNumOfUniqueInts([5,5,4], k = 1) == 1
assert s.findLeastNumOfUniqueInts([2,4,1,8,3,5,1,3], 3) == 3
