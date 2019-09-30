# -*- coding: utf-8 -*-
# https://leetcode.com/problems/reverse-integer/

class Solution:
    def reverse(self, x: int) -> int:
        str_temp = str(x)

        sign = 1
        if str_temp[0] == '-':
            sign = -1
            str_temp = str_temp[1:]

        str_temp = str_temp[::-1]

        answer = int(''.join(str_temp))
        answer = sign * answer
        if pow(2, 31) * -1 < answer < pow(2, 31)-1:
            return answer

        return 0



def test_solution():
    s = Solution()
    s.reverse("123")

    assert s.reverse(123) == 321
    assert s.reverse(-123) == -321
    assert s.reverse(120) == 21
    assert s.reverse(-1) == -1
    assert s.reverse(1534236469) == 0

s = Solution()
print(s.reverse(123))
