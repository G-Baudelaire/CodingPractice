from collections import defaultdict


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2) or set(word1) != set(word2):
            return False

        dictionary1 = defaultdict(int)
        dictionary2 = defaultdict(int)

        for char in word1:
            dictionary1[char] += 1

        for char in word2:
            dictionary2[char] += 1

        counts1 = list(dictionary1.values())
        counts2 = list(dictionary2.values())
        counts1.sort()
        counts2.sort()

        return counts1 == counts2
