from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        output = [0] * (n + 1)
        for i in range(n + 1):
            output[i] = self.count(i)

    def count(self, m):
        count = 0
        while m != 0:
            count += m % 2
            m = m >> 1
        return count
