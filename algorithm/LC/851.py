# -*- coding: utf-8 -*-
from typing import *
from collections import defaultdict


class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        def dfs(i):
            if ans[i] >= 0:
                return ans[i]
            ans[i] = i

            for j in money[i]:
                if quiet[ans[i]] > quiet[dfs(j)]:
                    ans[i] = ans[j]
            return ans[i]

        n = len(quiet)
        money = defaultdict(list)
        for i, j in richer:
            money[j].append(i)

        ans = [-1] * n
        for i in range(n):
            dfs(i)
        print(ans)
        return ans


s = Solution()
s.loudAndRich(richer=[[1, 0], [2, 1], [3, 1], [3, 7], [4, 3], [5, 3], [6, 3]], quiet=[3, 2, 5, 4, 6, 1, 7, 0])
