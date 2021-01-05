# -*- coding: utf-8 -*-
class Solution:
    def lengthOfLIS(self, nums):
        if len(nums) <= 0:
            return 0

        d = [0 for x in nums]
        d[0] = 1

        for i in range(1, len(nums)):
            max_value = 0
            for j in range(i):
                if nums[j] < nums[i] and d[j] > max_value:
                    max_value = d[j]

            d[i] = max_value + 1

        return max(d)



s = Solution()
# assert s.lengthOfLIS([10,9,2,5,3,7,101,18]) == 4
# assert s.lengthOfLIS([0,1,0,3,2,3]) == 4
# assert s.lengthOfLIS([7, 7, 7, 7]) == 1
# assert s.lengthOfLIS([-1, 0, 1, 2, -10, 4, 5]) == 4
assert s.lengthOfLIS([1,3,6,7,9,4,10,5,6]) == 6
