from typing import List


class OriginalSolution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]

        maximum_prefix_length = min(len(string) for string in strs)
        prefix_length = 0

        while maximum_prefix_length > prefix_length:
            for string in strs[1:]:
                if string[prefix_length] != strs[0][prefix_length]:
                    return strs[0][0:prefix_length]
            prefix_length += 1
        return strs[0][0:prefix_length]


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]

        prefix_length = min(len(string) for string in strs)
        for string1, string2 in zip(strs[:-1], strs[1:]):
            while string1[:prefix_length] != string2[:prefix_length]:
                prefix_length -= 1
        return strs[0][:prefix_length]

