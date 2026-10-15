class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n in (1,2):
            return n

        sequence_minus_2 = 1
        sequence_minus_1 = 2
        sequence_0 = None
        for _ in range(n - 2):
            sequence_0 = sequence_minus_1 + sequence_minus_2
            sequence_minus_2, sequence_minus_1 = sequence_minus_1, sequence_0
        return sequence_0