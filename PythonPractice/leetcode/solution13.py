# 13. Roman to Integer
class Solution:

    def romanToInt(self, s: str) -> int:
        symbol_values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        largest_value = 0
        total = 0

        for char in reversed(s):
            if symbol_values[char] < largest_value:
                total -= symbol_values[char]
            else:
                total += symbol_values[char]
                largest_value = symbol_values[char]
        return total
