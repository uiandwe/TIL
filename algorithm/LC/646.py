# -*- coding: utf-8 -*-
from operator import itemgetter

class Solution:
    def findLongestChain(self, pairs):
        s = sorted(pairs, key=itemgetter(1))

        d = [0] * len(s)
        d[0] = 1

        for i in range(len(s)):
            max_value = 0
            for j in range(i):
                if s[j][1] < s[i][0] and d[j] > max_value:
                    max_value = d[j]

            d[i] = max_value + 1

        return max(d)


s = Solution()
assert s.findLongestChain([[1,2], [2,3], [3,4]]) == 2
