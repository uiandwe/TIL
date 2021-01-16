# -*- coding: utf-8 -*-
class Solution:
    def longestCommonPrefix(self, strs) -> str:

        if len(strs) == 0:
            return ""

        ret = d = strs[0]
        for i in range(1, len(strs)):
           index = 0
           while index < len(d) and index < len(strs[i]):
               if d[index] != strs[i][index]:
                   break
               index += 1

           if len(ret) > len(d[:index]):
               ret = d[:index]
           elif index == 0:
               return ""

        return ret







s = Solution()
assert s.longestCommonPrefix(["flower", "flow", "flight"]) == "fl"
assert s.longestCommonPrefix(["dog", "racecar", "car"]) == ""
assert s.longestCommonPrefix(["dog", "dog"]) == "dog"
assert s.longestCommonPrefix(["", "b"]) == ""
assert s.longestCommonPrefix(["aaa", "aa", "aaa"]) == "aa"
