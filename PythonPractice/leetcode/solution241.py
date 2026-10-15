# Different Ways to Add Parentheses
# TODO
import re
from typing import List


class Solution:
    operator_map = {'+': lambda x, y: x + y, '-': lambda x, y: x - y, '*': lambda x, y: x * y}

    def diffWaysToCompute(self, expression: str) -> List[int]:
        values = list(map(int, re.split(r"[-+*]", expression)))
        operators = re.findall(r"[-+*]", expression)
        return self.iterative(values, operators)

    def recursion(self, values, operators):
        if len(values) == 1:
            return values

        output = list()
        for i in range(1, len(values)):
            front = self.recursion(values[:i], operators[:i - 1])
            back = self.recursion(values[i:], operators[i:])
            operator = self.operator_map[operators[i - 1]]
            output.extend(operator(f, b) for f in front for b in back)
        return output

    def iterative(self, values, operators):
        n = len(values)
        dp = [[[] for j in range(i+1)] for i in range(n)]
        for i in range(n):
            dp[i][i]  = [values[i]]

        for i in range(1, n):
            for j in reversed(range(i)):
                print("position ", i, j)
                for k in range(j, i):
                    print("others " ,j, k, i-j, i-k)

        print(dp)

if __name__ == '__main__':
    expression = "2*3-4*5"
    print(Solution().diffWaysToCompute(expression))
