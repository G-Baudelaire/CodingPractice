from typing import List


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        left, right = 0, len(nums) - 1
        count = 0

        while (left < right):
            summation = nums[left] + nums[right]
            if summation == k:
                left += 1
                right -= 1
                count += 1
            elif summation < k:
                left += 1
            else:
                right -= 1

        return count