# -*- coding: utf-8 -*-
from collections import Counter, defaultdict
class Solution:
    def minDeletions(self, s: str) -> int:
        d = Counter(s)

        a = sorted([[d[i], 0] for i in d], reverse=True)
        a[0][1] = a[0][0]
        ret = 0

        for i in range(1, len(a)):
            if a[i-1][1] <= a[i][0]:
                a[i][1] = min(a[i-1][1] - 1, a[i][0])

                if a[i][1] < 0:
                    a[i][1] = 0

            else:
                a[i][1] = a[i][0]
            ret += a[i][0] - a[i][1]

        return ret

s = Solution()
assert s.minDeletions("aaabbbcc") == 2
assert s.minDeletions("aab") == 0
assert s.minDeletions("ceabaacb") == 2
assert s.minDeletions("abcabc") == 3
assert s.minDeletions("bbcebab") == 2
