# Word Break
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        string_length = len(s)
        dynamic_array = [[False for _ in range(string_length + 1)] for _ in range(2)]
        dynamic_array[0][0] = True

        while any(dynamic_array[0][:string_length]) and not dynamic_array[0][-1]:
            for position in range(string_length):
                if not dynamic_array[0][position]:
                    continue

                for word in wordDict:
                    end = position + len(word)
                    if end > string_length + 1:
                        continue
                    elif s[position:end] == word:
                        dynamic_array[1][end] = True
                    else:
                        pass

            dynamic_array[0] = dynamic_array[1]
            dynamic_array[1] = [False for _ in range(string_length + 1)]
        return dynamic_array[0][-1]

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        s_length = len(s)
        word_set = set(wordDict)
        maxLength = max(len(word) for word in word_set)
        dynamic_array = [False] * (s_length + 1)
        dynamic_array[0] = True

        for i in range(1, s_length + 1):
            for j in range(1, min(maxLength, i) + 1):
                if not dynamic_array[i - j]:
                    continue

                if s[i - j: i] in word_set:
                    dynamic_array[i] = True
                    break

        return dynamic_array[s_length]


s = "leetcode"

wordDict = ["leet", "code"]

if __name__ == '__main__':
    print(Solution().wordBreak(s, wordDict))
