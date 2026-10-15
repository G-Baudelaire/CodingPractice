class Solution:
    def isValid(self, s: str) -> bool:
        stack = list()
        mapping = {'(':')', '{': '}', '[':']'}

        for character in s:
            if character in mapping:
                stack.append(character)
                continue

            if (not stack) or (mapping[stack.pop()] != character):
                return False

        return (not stack)