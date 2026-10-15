from typing import List

# Maximum Subarray

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum = 0
        maximum_sum = -float("inf")

        for number in nums:
            current_sum = max(current_sum + number, number)
            maximum_sum = max(maximum_sum, current_sum)
        return maximum_sum


if __name__ == '__main__':
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4] # Expect 6
    nums = [1] # Expect 1
    nums = [5, 4, -1, 7, 8] # Expect 23
    print(Solution().maxSubArray(nums))
