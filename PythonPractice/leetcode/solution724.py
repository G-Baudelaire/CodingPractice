from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left, right = 0, sum(nums)

        for index, num in enumerate(nums):
            if index != 0:
                left += nums[index - 1]

            right -= nums[index]

            if left == right:
                return index

        return -1
