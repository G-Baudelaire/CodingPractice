class Solution:
    vowels = {"a", "e", "i", "o", "u"}

    def maxVowels(self, s: str, k: int) -> int:
        if len(s) <= k:
            return sum(map(lambda x: x in self.vowels, s))

        count = sum(map(lambda x: x in self.vowels, s[:k]))
        max_count = count

        for index in range(len(s) - k):
            count -= s[index] in self.vowels
            count += s[index + k] in self.vowels
            max_count = max(max_count, count)

        return max_count
