# -*- coding: utf-8 -*-
from typing import *
class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        for i in range(1, n//2+1):
            temp = [i, n-i]
            s1 = str(temp[0])
            s2 = str(temp[1])
            if s1.find('0') == -1 and s2.find('0') == -1:
                # print(temp)
                return temp
s = Solution()
s.getNoZeroIntegers(2)
s.getNoZeroIntegers(11)
s.getNoZeroIntegers(10000)
s.getNoZeroIntegers(69)
s.getNoZeroIntegers(1010)
