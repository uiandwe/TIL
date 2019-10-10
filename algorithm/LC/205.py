# -*- coding: utf-8 -*-
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d = {}

        for a, b in zip(s, t):
            if a in d.keys():
                if d[a] != b:
                    return False
            else:
                if b in d.values():
                    return False
                d[a] = b
        return True

s = Solution()
print(s.isIsomorphic("egg", "add"))
print(s.isIsomorphic("foo", "bar"))
print(s.isIsomorphic("paper", "title"))
print(s.isIsomorphic("ab", "aa"))
print(s.isIsomorphic("aba", "baa"))
