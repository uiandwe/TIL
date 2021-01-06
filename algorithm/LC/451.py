# -*- coding: utf-8 -*-
from collections import defaultdict, Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        d = Counter(s)

        def k(x):
            return d[x]

        r = list(s)
        r.sort()
        r.sort(key=k, reverse=True)

        return ''.join(r)



s = Solution()
# assert s.frequencySort("tree") == "eetr"
# assert s.frequencySort("Aabb") == "bbAa"
assert s.frequencySort("loveleetcode") == "eeeeoollvtdc"

