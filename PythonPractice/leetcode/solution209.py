# Minimum Size Subarray Sum
from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        current_sum = 0
        min_len = float('inf')

        for right in range(len(nums)):
            current_sum += nums[right]

            # Contract the window as long as the current sum meets the target
            while current_sum >= target:
                min_len = min(min_len, right - left + 1)
                current_sum -= nums[left]
                left += 1

        return min_len if min_len != float('inf') else 0

if __name__ == '__main__':
    target = 4
    nums = [1,4,4]
    print(Solution().minSubArrayLen(target, nums))
