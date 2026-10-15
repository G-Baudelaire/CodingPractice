from itertools import accumulate
from typing import List


class Solution:
    def trap(self, heights: List[int]) -> int:
        left_maxes = [i for i in accumulate(heights, max)]
        right_maxes = [i for i in accumulate(heights[::-1], max)][::-1]
        result = 0

        for i in range(1, len(heights) - 1):
            result += max(min(left_maxes[i - 1], right_maxes[i + 1]) - heights[i], 0)

        return result
