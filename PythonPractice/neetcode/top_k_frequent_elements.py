from collections import Counter
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        sorted_counts = sorted(counts.items(), key=lambda item: item[1], reverse=True)
        k_most_frequent = [number for number, _ in sorted_counts[:k]]
        return k_most_frequent
