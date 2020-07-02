class Solution:
    def findMaxConsecutiveOnes(self, nums) -> int:
        result = 0
        temp = 0
        for i in nums:
            if i == 0:
                result = max(result, temp)
                temp = 0
            else:
                temp += 1

        return max(result, temp)

s = Solution()
print(s.findMaxConsecutiveOnes([1,0,1,1,0,1]))
print(s.findMaxConsecutiveOnes([0]))
print(s.findMaxConsecutiveOnes([0, 0, 0]))
print(s.findMaxConsecutiveOnes([0, 0, 1]))
