from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        prev1, prev2 = 0, 0
        for i in range(len(nums)):
            dp[i] = max(prev1, prev2 + nums[i])
            prev1, prev2 = dp[i], prev1
        return dp[-1]
