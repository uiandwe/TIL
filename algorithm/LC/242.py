# -*- coding: utf-8 -*-
import collections


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        d1 = collections.Counter(s)
        d2 = collections.Counter(t)

        for key in d1.keys():
            if key not in d2.keys():
                return False
            if d2[key] != d1[key]:
                return False

        return True
