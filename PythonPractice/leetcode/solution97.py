# Interleaving String
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        # Initialise Table
        dp = [False] * (len(s2) + 1)

        dp[0] = True
        for j in range(1, len(s2) + 1):
            dp[j] = dp[j - 1] and s2[j - 1] == s3[j - 1]

        for i in range(1, len(s1) + 1):
            dp[0] = dp[0] and s1[i - 1] == s3[i - 1]
            for j in range(1, len(s2) + 1):
                s1_increment = dp[j - 1] and s2[j - 1] == s3[i + j - 1]
                s2_increment = dp[j] and s1[i - 1] == s3[i + j - 1]
                dp[j] = s1_increment or s2_increment
        return dp[-1]
if __name__ == '__main__':
    s1 = "aabcc"
    s2 = "dbbca"
    s3 = "aadbbcbcac"
    solution = Solution().isInterleave(s1, s2, s3)
    print(solution)
