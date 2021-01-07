# -*- coding: utf-8 -*-
class Solution:
    def sortString(self, s: str) -> str:
        s = list(s)
        result = []
        flag = True
        while s:
            temp = sorted(set(s))
            if not flag:
                temp = sorted(set(s), reverse=True)

            for ch in temp:
                s.remove(ch)
            result.extend(temp)
            flag = not flag

        return ''.join(result)

s = Solution()
assert s.sortString("aaaabbbbcccc") == "abccbaabccba"
