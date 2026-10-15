from typing import List


class Solution:
    character_mapping = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
    }

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        elif len(digits) == 1:
            return list(self.character_mapping[digits])

        digit = digits[-1]
        prefixes = self.letterCombinations(digits[:-1])
        return list(prefix + char for char in self.character_mapping[digit] for prefix in prefixes)


print(Solution().letterCombinations("23"))
