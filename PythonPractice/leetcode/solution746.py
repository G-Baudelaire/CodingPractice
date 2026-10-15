from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0] * len(cost)

        for step in range(3, len(cost)):
            dp[step] = min(dp[step - 2] + cost[step - 2], dp[step - 1] + cost[step - 1])

        return min(dp[-2] + cost[-2], dp[-1] + cost[-1])
