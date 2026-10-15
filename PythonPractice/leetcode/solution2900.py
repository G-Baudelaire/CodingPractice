from typing import List


class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        current = None
        result = []
        for word, group in zip(words, groups):
            if group != current:
                current = group
                result.append(word)
        return result

