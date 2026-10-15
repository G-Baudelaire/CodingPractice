from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        right = 0
        max_width = 0
        total = nums[0]

        while True:
            width = right - left + 1
            zeros = width - total
            if zeros <= k:
                max_width = width
            else:
                total -= nums[left]
                left += 1

            right += 1
            if right == len(nums): break
            total += nums[right]

        return max_width
