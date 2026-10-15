class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {"A", "E", "I", "O", "U", "a", "e", "i", "o", "u"}
        stack = [char for char in s if char in vowels]

        output = ""
        for index in range(len(s)):
            if s[index] not in vowels:
                output += s[index]
            else:
                output += stack.pop()

        return output
