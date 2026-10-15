class Solution:
    def longestPalindrome(self, s: str) -> str:
        return_data = (0, 0)  # (Index, Length)
        len_of_string = len(s)
        dp = [0] * (len_of_string + 1)

        for end in range(len_of_string):
            for start in range(end + 1):
                word_length = end - start + 1
                if word_length == 1:
                    dp[start] = 1
                elif dp[start + 1] == word_length - 2 and s[start] == s[end]:
                    dp[start] = dp[start + 1] + 2
                    if return_data[1] < dp[start]:
                        return_data = (start, dp[start])

        return s[return_data[0]:return_data[0] + dp[return_data[0]]]

# Generated
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s or len(s) == 1:
            return s  # Handle edge cases directly

        start, max_len = 0, 0

        def expand_around_centre(left: int, right: int):
            nonlocal start, max_len
            while left >= 0 and right < len(s) and s[left] == s[right]:
                current_len = right - left + 1
                if current_len > max_len:
                    max_len = current_len
                    start = left
                left -= 1
                right += 1

        for i in range(len(s)):
            expand_around_centre(i, i)  # Odd-length palindrome
            expand_around_centre(i, i + 1)  # Even-length palindrome

        return s[start:start + max_len]
s = "cbbd"
print(Solution().longestPalindrome(s))
