# -*- coding: utf-8 -*-
from typing import *
from collections import Counter

class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        ret = []
        for word in d:

            index1 = 0
            index2 = 0

            while index1 < len(s) and index2 < len(word):
                if s[index1] == word[index2]:
                    index2 += 1
                index1 += 1
            if index2 == len(word):
                ret.append((word, index2))

        if len(ret) == 0:
            return ""

        ret.sort(key=lambda x: (-x[1], x[0]))

        return ret[0][0]




s = Solution()
assert s.findLongestWord(s = "abpcplea", d = ["ale","apple","monkey","plea"]) == "apple"
assert s.findLongestWord(s = "aaa", d = ["aaa","apple","monkey","plea"]) == "aaa"
assert s.findLongestWord(s = "aewfafwafjlwajflwajflwafj", d = ["apple","ewaf","awefawfwaf","awef","awefe","ewafeffewafewf"]) == "ewaf"
assert s.findLongestWord(s = "apple", d = ["zxc","vbn"]) == ""

