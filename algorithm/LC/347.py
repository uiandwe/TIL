# -*- coding: utf-8 -*-
from collections import Counter
import operator

class Solution:
    def topKFrequent(self, nums, k: int):
        d = Counter(nums)
        s = sorted(d.items(), key=operator.itemgetter(1), reverse=True)
        answer = [s[i][0] for i in range(k)]
        return answer


s= Solution()
s.topKFrequent([1, 1, 1, 2, 2, 3], 2)
