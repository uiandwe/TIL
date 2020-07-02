class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        l = len(nums)
        total = (l * (l+1)) // 2
        
        for i in nums:
            total -= i
            
        return total
