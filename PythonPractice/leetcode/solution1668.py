class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        length = len(word)
        left, right = 0, length
        result = 0

        while right <= len(sequence):
            substring = sequence[left:right]
            if substring + word == word + substring:
                result += 1
                right += length
            else:
                left += 1
                right += 1

        return result