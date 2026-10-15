class Solution:
    def tribonacci(self, n: int) -> int:
        dp = [0, 1, 1]

        if n in (0, 1, 2):
            return dp[n]

        for _ in range(n - 2):
            dp = [dp[1], dp[2], sum(dp)]

        return dp[-1]
