class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        count = 0

        while n != 0 and count == 0:
            count += n & 0b1
            if n & 0b10 == 0b10:
                return False
            n >>= 2

        return n == 0 and count == 1
