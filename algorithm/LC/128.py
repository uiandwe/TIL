# -*- coding: utf-8 -*-
class Solution:
    def longestConsecutive(self, nums):
        if not nums:
            return 0

        nums.sort()
        print(nums)

        answer = 1
        c = 1

        for i in range(1, len(nums)):
            if nums[i-1] == nums[i]-1:
                c += 1
            elif nums[i - 1] == nums[i]:
                continue
            else:
                answer = max(answer, c)
                c = 1

        return max(answer, c)



s = Solution()
print(s.longestConsecutive([100, 4, 200, 1, 3, 2]))
print(s.longestConsecutive([0, -1]))
print(s.longestConsecutive([9,1,4,7,3,-1,0,5,8,-1,6]))
print(s.longestConsecutive([1,2,0,1]))



