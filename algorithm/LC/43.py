# -*- coding: utf-8 -*-
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if len(num1) == 0 or len(num2) == 0 or num1[0] == "0" or num2[0] == "0":
            return "0"

        ret = [0] * (len(num1) + len(num2))
        for i, n1 in enumerate(num1[::-1]):
            for j, n2 in enumerate(num2[::-1]):
                val = ret[i+j]+int(n1) * int(n2)
                ret[i+j] = val % 10
                ret[i+j+1] += val // 10

        ret = list(map(lambda x: str(x), ret))
        return ''.join(ret)[::-1].lstrip('0')

s = Solution()
assert s.multiply("2", "3") == "6"
assert s.multiply("123", "456") == "56088"
assert s.multiply("123", "0") == "0"
assert s.multiply("7", "871") == "6097"
