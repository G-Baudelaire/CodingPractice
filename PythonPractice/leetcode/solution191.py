# Number of 1 Bits

class Solution:
    def hammingWeight(self, n: int) -> int:
        tally = 0

        while n > 0:
            if n & 1:
                tally += 1
            n = n >> 1

        return tally
