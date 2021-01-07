# -*- coding: utf-8 -*-
from operator import itemgetter
from collections import defaultdict

class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:

        memo = {1: 0}

        def kth(x):
            if x % 2 == 0:
                return x // 2
            else:
                return 3 * x + 1

        d = []
        for i in range(lo, hi+1):
            temp = i
            count = 1
            while True:
                temp = kth(temp)
                if temp == 1:
                    memo[i] = count
                    d.append((i, memo[i]))
                    break
                elif temp in memo.keys():
                    memo[i] = count + memo[temp]
                    d.append((i, memo[i]))
                    break
                count += 1

        keys = sorted(d, key=itemgetter(1, 0))
        return keys[k-1][0]



s = Solution()
assert s.getKth(lo = 12, hi = 15, k = 2) == 13
assert s.getKth(lo = 7, hi = 11, k = 4) == 7
assert s.getKth(lo = 10, hi = 20, k = 5) ==  13
assert s.getKth(lo = 1, hi = 1000, k = 777) == 570
