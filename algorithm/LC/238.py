# -*- coding: utf-8 -*-
class Solution:
    def productExceptSelf(self, nums):
        d = [0 for i in nums]
        answer = d[0] = nums[0]

        for i in range(1, len(nums)):
            d[i] = answer
            answer = answer * nums[i]

        answer = nums[len(nums)-1]
        for i in reversed(range(len(nums)-1)):
            d[i] *= answer
            answer = answer * nums[i]
        if nums[0] != 0:
            d[0] //= nums[0]
        return d


s = Solution()
print(s.productExceptSelf([1, 2, 3, 4]))
print(s.productExceptSelf([9, 0, -2]))
print(s.productExceptSelf([4, 3, 2, 1, 2]))

"""
1 2 3 4 
0 1 2 6
      6



1 1 2 6

9 0 -2
0 9 0



"""
