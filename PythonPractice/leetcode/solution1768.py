class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        pointer1, pointer2 = 0, 0
        len_word1, len_word2 = len(word1), len(word2)
        output = ""

        while pointer1 < len_word1 and pointer2 < len_word2:
            output += word1[pointer1] + word2[pointer2]
            pointer1 += 1
            pointer2 += 1

        while pointer1 < len_word1 :
            output += word1[pointer1]
            pointer1 += 1

        while  pointer2 < len_word2:
            output +=  word2[pointer2]
            pointer2 += 1

        return output
