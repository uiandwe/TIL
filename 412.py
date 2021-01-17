# -*- coding: utf-8 -*-
from typing import *


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        d = []
        for i in range(1, n+1):
            temp = str(i)
            if i % 3 == 0:
                temp = "Fizz"
            if i % 5 == 0:
                temp = "Buzz"
            if i % 3 == 0 and i % 5 == 0:
                temp = "FizzBuzz"

            d.append(temp)

        print(d)


s = Solution()
s.fizzBuzz(15)
