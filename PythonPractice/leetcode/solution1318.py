class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        count = 0
        while a or b or c:
            bit_a, bit_b, bit_c = a & 1, b & 1, c & 1
            if bit_c:
                count += not (bit_a or bit_b)
            else:
                count += bit_a + bit_b

            a >>= 1
            b >>= 1
            c >>= 1
        return count
