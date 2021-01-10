from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1

        left, right = 0, len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2

            if nums[mid] < nums[right]:
                right = mid - 1
            else:
                left = mid + 1

        pivot = left
        print(pivot)

        left, right = 0, len(nums) - 1
        if nums[pivot] <= target <= nums[right]:
            left = pivot
        else:
            right = pivot

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return mid

        return -1


        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            elif target >= nums[mid]:
                if nums[mid] < nums[left] and target >= nums[left]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[right] < nums[mid] and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1




s = Solution()
assert s.search(nums = [4,5,6,7,0,1,2], target = 0) == 4
assert s.search(nums = [4,5,6,7,0,1,2], target = 3) == -1
assert s.search(nums = [1], target = 0) == -1

