class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        temp = 0
        max_value = float('-inf')

        if len(nums) == 1:
            return nums[0]

        for i in range(len(nums)):
            temp += nums[i]

            if temp > max_value:
                max_value = temp
            if temp < 0:
                temp = 0

        return max_value

s = Solution()
print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
