from collections import defaultdict
from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dictionary = defaultdict(int)
        for num in arr:
            dictionary[num] += 1
        return len(set(dictionary.values())) == len(dictionary)
