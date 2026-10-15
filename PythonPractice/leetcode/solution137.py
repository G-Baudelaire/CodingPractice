# Single Number
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        bit_counts = [0] * 32
        for num in nums:
            for i in range(32):
                bit_value = (num >> i) & 1
                # Fill bits from the most significant (index 0) to least significant
                bit_counts[-(1 + i)] = (bit_counts[-(1 + i)] + bit_value) % 3

        output = 0
        for bit in bit_counts:
            output = (output << 1) | bit

        # Adjust for negative numbers: if the sign bit is set, subtract 2^32
        if output >= 2 ** 31:
            output -= 2 ** 32

        return output
