# -*- coding: utf-8 -*-
import itertools


class Solution:
    def permute(self, nums):
        # return list(itertools.permutations(nums))
        group = []

        def dfs(arr):

            if len(arr) == len(nums):
                group.append(tuple(arr))
                return

            for i in nums:
                if not i in arr:
                    arr.append(i)
                    dfs(arr)
                    arr.pop()

        for i in nums:
            dfs([i])

        return group
s = Solution()
print(s.permute([1, 2, 3]))
