# -*- coding: utf-8 -*-
class Solution:
    def countAndSay(self, n: int) -> str:

        s = "1"

        for _ in range(1, n):
            ret = ""
            cnt = 1
            ch = s[0]
            for i in range(1, len(s)):
                if ch == s[i]:
                    cnt += 1
                else:
                    ret += str(cnt) + ch
                    cnt = 1
                    ch = s[i]
            s = ret + str(cnt) + ch

        return s




s = Solution()
assert s.countAndSay(1) == "1"
assert s.countAndSay(2) == "11"
assert s.countAndSay(3) == "21"
assert s.countAndSay(4) == "1211"
assert s.countAndSay(5) == "111221"
assert s.countAndSay(6) == "312211"
assert s.countAndSay(7) == "13112221"
assert s.countAndSay(8) == "1113213211"
