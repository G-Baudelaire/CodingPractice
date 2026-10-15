from collections import deque


class Solution:
    def calculate(self, s: str) -> int:
        return self.calculate2(deque(s))

    def calculate2(self, s: deque[str]) -> int:
        current_value = result = 0
        sign = 1

        while s:
            char = s.popleft()
            if char.isdigit():
                current_value = current_value * 10 + int(char)
            elif char in {"+", "-"}:
                result += sign * current_value
                sign = 1 if char == "+" else -1
                current_value = 0
            elif char == "(":
                current_value = self.calculate2(s)
            elif char == ")":
                break
            elif char == " ":
                pass
            else:
                raise Exception("Incorrect character input")
        return result + sign * current_value
