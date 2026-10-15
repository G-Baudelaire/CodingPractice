class Solution:
    def fib(self, n: int) -> int:
        if n == 0: return 0

        previous, current = 0, 1
        for i in range(n - 1):
            previous, current = current, current + previous
        return current
