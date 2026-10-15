# Add Binary

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        foo = bin(a, 2)
        bar = bin(b, 2)

        return bin(foo + bar)
