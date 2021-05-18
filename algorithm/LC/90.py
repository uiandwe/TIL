# -*- coding: utf-8 -*-
from typing import List
import itertools
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        arr = set(())

        for i in range(1, len(nums)+1):

            l = list(itertools.combinations(nums, i))
            for o in l:
                arr.add(tuple(sorted(list(o))))
        arr.add(())
        # print(arr)
        return arr



s = Solution()
# s.subsetsWithDup(nums = [1,2,2])
s.subsetsWithDup([4,4,4,1,4])
