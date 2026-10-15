class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        alphabet_count = [0] * 26

        for character in s:
            index = self.convert_alphabet(character)
            alphabet_count[index] += 1

        for character in t:
            index = self.convert_alphabet(character)
            alphabet_count[index] -= 1

        return any(alphabet_count)

    def convert_alphabet(self, c: str):
        return ord(c) - ord('a')
