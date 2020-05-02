# -*- coding: utf-8 -*-
from collections import Counter
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        d1 = Counter(J)
        d2 = Counter(S)

        answer = 0
        for i in list(d1.keys() & d2.keys()):
            answer += d2[i]

        return answer

s = Solution()
print(s.numJewelsInStones("aA", "aAAbbbbb"))
print(s.numJewelsInStones("z", "ZZ"))
