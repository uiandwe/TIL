# -*- coding: utf-8 -*-
# https://leetcode.com/problems/reverse-integer/

class Solution:
    def reverse(self, x: int) -> int:
        s = str(x)
        if s[0] == '-':
            s = int(s[1:][::-1]) * -1
        else:
            s = int(s[::-1])

        if pow(2, 31) * -1 < s < pow(2, 31) - 1:
            return s

        return 0


#
# def test_solution():
#     s = Solution()
#     s.reverse("123")
#
#     assert s.reverse(123) == 321
#     assert s.reverse(-123) == -321
#     assert s.reverse(120) == 21
#     assert s.reverse(-1) == -1
#     assert s.reverse(1534236469) == 0

s = Solution()
print(s.reverse(123))
print(s.reverse(-123))
print(s.reverse(-120))
print(s.reverse(1534236469))


