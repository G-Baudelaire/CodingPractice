class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1] * n
        for _ in range(m - 1):
            for i in range(n):
                left = dp[i - 1] if i != 0 else 0
                up = dp[i]
                dp[i] = left + up
        return dp[-1]
