class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) in [0, 1]:
            return len(s)

        window_start, window_end = 0, 0
        window_size = 0

        while window_end <= len(s):
            window = s[window_start:window_end]

            if window_size == len(set(window)):
                window_size += 1
            else:
                window_start += 1

            window_end += 1

        return window_size - 1


s = "abcabcbb"
print(Solution().lengthOfLongestSubstring(s))
