# -*- coding: utf-8 -*-
from collections import defaultdict
from typing import *


class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        hm = {}
        for i in range(len(favoriteCompanies)):
            for j in favoriteCompanies[i]:
                if j in hm:
                    hm[j].append(i)
                else:
                    hm[j] = [i]
        ans = []
        for i in range(len(favoriteCompanies)):
            b = set(hm[favoriteCompanies[i][0]])
            for j in favoriteCompanies[i][1:]:
                b = b & set(hm[j])
            if len(b) == 1:
                ans.append(i)
        return ans

s = Solution()
s.peopleIndexes([[ "leetcode", "facebook"], [ "leetcode", "google", "facebook"]]) == [0, 1, 4]


