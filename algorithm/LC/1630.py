# -*- coding: utf-8 -*-
from typing import  *
class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        d = []
        for i, j in zip(l, r):
            temp = sorted(nums[i:j+1])
            difference = abs(temp[0] - temp[1])
            ret = True
            for k in range(2, len(temp)):
                if abs(temp[k-1] - temp[k]) != difference:
                    ret = False
                    break
            d.append(ret)

        return d



s = Solution()
s.checkArithmeticSubarrays(nums = [4,6,5,9,3,7], l = [0,0,2], r = [2,3,5])
s.checkArithmeticSubarrays(nums = [-12, -9, -3, -12, -6,15,20, -25, -20, -15, -10], l = [0,1,6,4,8, 7], r = [4,4,9,7,9,10])
