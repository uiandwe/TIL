class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) < 1:
            return 0

        if len(nums) == 1:
            return nums[0]

        if len(nums) == 2:
            return max(nums)

        d = [0 for x in nums]
        d[0] = nums[0]
        d[1] = nums[1]

        for i in range(2, len(nums)):
            d[i] = max(d[i - 2] + nums[i], d[i - 3] + nums[i])

        return max(d)


        last, now = 0, 0
        for i in nums:
            last, now = now, max(last + i, now)
        return now


s = Solution()
print(s.rob([1,2,3,1]))
print(s.rob([2,7,9,3,1]))
print(s.rob([2, 1, 1, 2]))
print(s.rob([1,1,1]))
print(s.rob([1,7,9,2]))
