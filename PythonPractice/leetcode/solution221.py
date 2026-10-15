class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0

        num_of_rows = len(matrix)
        num_of_columns = len(matrix[0])
        max_side = 0
        prev = 0
        dp = [0] * (num_of_columns + 1)

        for i in range(1, num_of_rows + 1):
            for j in range(1, num_of_columns + 1):
                temp = dp[j]
                if matrix[i - 1][j - 1] == '1':
                    dp[j] = min(dp[j], dp[j - 1], prev) + 1
                    max_side = max(max_side, dp[j])
                else:
                    dp[j] = 0
                prev = temp

        return max_side * max_side