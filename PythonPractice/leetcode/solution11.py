import operator
from functools import reduce


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # Unnecessarily hard to read but it was fun to write
        return chr(reduce(operator.xor, map(ord, s + t), 0))

if __name__ == '__main__':
    Solution().findTheDifference("abc", "abcd")
