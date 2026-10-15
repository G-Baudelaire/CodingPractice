# Bitwise and of numbers range

class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        state = 0

        for i in range(32):
            state = (state << 1) | 1

        for i in range(left, right + 1):
            state &= i
        return state


if __name__ == '__main__':
    left = 5
    right = 7
    print(Solution().rangeBitwiseAnd(left, right))
