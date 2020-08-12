# -*- coding: utf-8 -*-
import collections


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d = collections.Counter(nums)
        for key in d.keys():
            if d[key] > 1:
                return True

        return False
