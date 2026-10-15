class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        count = 0

        while n != 0 and count < 2:
            count += n & 1
            n >>= 1

        return count == 1

if __name__ == '__main__':
    Solution().isPowerOfTwo(0)
