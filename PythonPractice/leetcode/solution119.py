from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        dp = [0] * (rowIndex + 1)
        dp[0] = 1
        for i in range(rowIndex):
            previous = 0
            for j in range(i + 2):
                dp[j], previous = dp[j] + previous, dp[j]
        return dp
