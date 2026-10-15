class SomewhatOptimisedSolution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        return self._numDistinct(s, t, 0, 0, dict())

    def _numDistinct(self, s, t, s_index, t_index, memory):
        try:
            return memory[(s_index, t_index)]
        except KeyError:
            pass

        if t_index == len(t):
            memory.update({(s_index, t_index): 1})
            return 1

        if s_index == len(s):
            memory.update({(s_index, t_index): 0})
            return 0

        if s[s_index] == t[t_index]:
            value = (self._numDistinct(s, t, s_index + 1, t_index + 1, memory) +
                     self._numDistinct(s, t, s_index + 1, t_index, memory))
        else:
            value = self._numDistinct(s, t, s_index + 1, t_index, memory)

        memory.update({(s_index, t_index): value})
        return value


class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        m, n = len(s), len(t)

        # Edge case: if t is an empty string, there is exactly one matching subsequence.
        if n == 0:
            return 1

        # Edge case: if s is an empty string and t is not, there are no subsequences of s that match t.
        if m == 0:
            return 0

        # dp[i][j] will store the number of distinct subsequences of s[:i] that match t[:j].
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # Every string s[:i] has exactly one subsequence (empty) that matches an empty t.
        for i in range(m + 1):
            dp[i][0] = 1

        # Fill the dp table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s[i - 1] == t[j - 1]:
                    # If characters match, add both possibilities:
                    # 1. Use the character in s (match this character with t)
                    # 2. Don't use the character in s (skip it)
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
                else:
                    # If characters don't match, skip the character in s.
                    dp[i][j] = dp[i - 1][j]

        # The bottom-right cell contains the number of distinct subsequences.
        return dp[m][n]

s = "babgbag"
t = "bag"
print(Solution().numDistinct(s, t))
