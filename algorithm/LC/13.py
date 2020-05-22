# -*- coding: utf-8 -*-
class Solution:
    def romanToInt(self, s: str) -> int:
        pre, ans = None, 0
        dic = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000, None: 10000}
        for c in s:

            if dic[pre] >= dic[c]:
                ans += dic[c]
            else:
                ans += dic[c] - dic[pre] * 2

            pre = c
        return ans



s = Solution()
assert s.romanToInt("III") == 3
assert s.romanToInt("I") == 1
assert s.romanToInt("IV") == 4
assert s.romanToInt("VI") == 6
assert s.romanToInt("VIII") == 8
assert s.romanToInt("IX") == 9
assert s.romanToInt("X") == 10
assert s.romanToInt("XI") == 11
assert s.romanToInt("XV") == 15
assert s.romanToInt("XIV") == 14
assert s.romanToInt("XIX") == 19
assert s.romanToInt("XX") == 20
assert s.romanToInt("XXXV") == 35
assert s.romanToInt("XL") == 40
assert s.romanToInt("XLV") == 45
assert s.romanToInt("XLIX") == 49
assert s.romanToInt("CM") == 900
assert s.romanToInt("DCCC") == 800
assert s.romanToInt("CMXCIX") == 999


