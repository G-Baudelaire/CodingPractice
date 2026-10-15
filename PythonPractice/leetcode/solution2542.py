import heapq
from typing import List


class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        nums = sorted(((num1, num2) for num1, num2 in zip(nums1, nums2)), key=lambda pair: pair[1], reverse=True)
        total = 0
        max_value = 0
        heap = []
        for add_value, multiple in nums:
            heapq.heappush(heap, add_value)
            total += add_value

            if k < len(heap):
                minimum_value = heapq.heappop(heap)
                total -= minimum_value

            if k == len(heap):
                max_value = max(max_value, total * multiple)

        return max_value