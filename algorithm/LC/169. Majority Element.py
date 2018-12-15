class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict = {}
        max_count = 0
        max_char = 0
        for i in nums:
            if i in dict:
                dict[i] += 1
            else:
                dict[i] = 1

            if dict[i] > max_count:
                max_count = dict[i]
                max_char = i

        return max_char



s = Solution()
print(s.majorityElement([3,2,3]))
print(s.majorityElement([3,3,4]))
