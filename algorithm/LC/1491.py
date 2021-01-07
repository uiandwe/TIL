# -*- coding: utf-8 -*-
from typing import *
class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        d = salary[1:-1]

        return sum(d) / len(d)

s = Solution()
assert s.average([4000,3000,1000,2000]) == 2500
assert s.average([6000,5000,4000,3000,2000,1000]) == 3500
assert s.average([8000,9000,2000,3000,6000,1000]) == 4750.00000

