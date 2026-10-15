from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        total = sum(nums[:k])
        max_total = total

        for left, right in zip(nums, nums[k:]):
            total = total - left + right
            max_total = max(max_total, total)

        return max_total / k
