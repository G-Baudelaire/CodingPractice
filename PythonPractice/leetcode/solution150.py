from collections import deque
from typing import List


class Solution:
    OPERATORS = {"+", "-", "*", "/"}

    def __init__(self):
        self._integer_stack = deque()

    def evalRPN(self, tokens: List[str]) -> int:
        for token in tokens:
            if token in self.OPERATORS:
                self._update_integer_stack(token)
            else:
                self._integer_stack.append(int(token))
        return self._integer_stack.pop()

    def _update_integer_stack(self, token):
        value2 = self._integer_stack.pop()
        value1 = self._integer_stack.pop()
        result = None
        match token:
            case "+":
                result = value1 + value2
            case "-":
                result = value1 - value2
            case "*":
                result = value1 * value2
            case "/":
                result = int(value1 / value2)
            case _:
                raise Exception("Invalid Operation")
        self._integer_stack.append(result)
