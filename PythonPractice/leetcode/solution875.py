import math
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        minimum, maximum = 0, max(piles)
        while minimum < maximum:
            middle = (maximum + minimum) // 2
            hours_taken = sum(map(lambda x: math.ceil(x / middle), piles))
            if hours_taken >= h:
                maximum = middle
            else:
                minimum = middle + 1
        return minimum
