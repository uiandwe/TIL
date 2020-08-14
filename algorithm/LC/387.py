# -*- coding: utf-8 -*-
import collections

class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = collections.Counter(s)

        for i, v in enumerate(s):
            print(i, v)
