from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if k == n:
            return [[i for i in range(n, 0, -1)]]
        elif k == 1:
            return [[i] for i in range(n, 0, -1)]

        output = []
        output.extend([[n] + end for end in self.combine(n - 1, k - 1)])
        output.extend(self.combine(n - 1, k))
        return output


n = 2
k = 2
for n in range(k, 5):
    print(Solution().combine(n, k))
