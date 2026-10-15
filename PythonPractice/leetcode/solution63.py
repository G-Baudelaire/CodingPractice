# Unique Paths
from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # Initialise DP Array
        dp = [0] * len(obstacleGrid[0])

        dp[0] = 1 if obstacleGrid[0][0] == 0 else 0

        for i in range(1, len(dp)):
            if obstacleGrid[0][i] == 0:
                dp[i] = dp[i - 1]

        for i in range(1, len(obstacleGrid)):
            dp[0] = dp[0] if obstacleGrid[i][0] == 0 else 0
            for j in range(1, len(dp)):
                dp[j] = dp[j - 1] + dp[j] if obstacleGrid[i][j] == 0 else 0

        return dp[-1]


if __name__ == '__main__':
    obstacleGrid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    Solution().uniquePathsWithObstacles(obstacleGrid)
