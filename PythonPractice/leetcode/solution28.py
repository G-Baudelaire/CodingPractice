class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        needle_length = len(needle)
        haystack_length = len(haystack)

        if haystack_length < needle_length:
            return -1

        for index in range(haystack_length - needle_length):
            if haystack[index: needle_length] == needle:
                return index