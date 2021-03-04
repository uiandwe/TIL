# -*- coding: utf-8 -*-

class Solution:
    def countAndSay(self, n: int) -> str:

        s = "1"

        for _ in range(1, n):
            temp = ""
            now = s[0]
            count = 1
            for i in range(1, len(s)):
                if now != s[i] and count > 0:
                    temp += str(count) + now
                    now = s[i]
                    count = 1
                else:
                    count += 1

            temp += str(count) + now
            s = temp
        # print(s)
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
