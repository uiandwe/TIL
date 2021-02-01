# -*- coding: utf-8 -*-
from typing import *
from collections import defaultdict
class Solution:
    def totalFruit(self, tree: List[int]) -> int:

        count = 1
        d = defaultdict(int)
        i = 1
        while i < len(tree):
            l = i - 1
            r = i + 1
            d = defaultdict(int)
            d[tree[i]] = 1

            while 0 <= l:
                d[tree[l]] += 1
                if len(d.keys()) >= 3:
                    del d[tree[l]]
                    break
                l -= 1

            while r < len(tree):
                d[tree[r]] += 1
                if len(d.keys()) >= 3:
                    del d[tree[r]]
                    break
                r += 1

            count = max(count, sum(d.values()))
            if count == len(tree) or r == len(tree):
                break
            i = r + 1

        count = max(count, sum(d.values()))
        # print(count, d)
        return count


s = Solution()
assert s.totalFruit([0]) == 1
assert s.totalFruit([1, 2, 1]) == 3
assert s.totalFruit([0, 1, 2, 1]) == 3
assert s.totalFruit([1, 2, 3, 2, 2]) == 4
assert s.totalFruit([1, 2, 3, 2, 2]) == 4
assert s.totalFruit([1, 0, 0, 2, 2]) == 4
assert s.totalFruit([3,3,3,1,2,1,1,2,3,3,4]) == 5
assert s.totalFruit([0,1,6,6,4,4,6]) == 5




