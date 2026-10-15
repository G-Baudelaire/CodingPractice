class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_dict = dict()
        for char in magazine:
            magazine_dict[char] = 1 + magazine_dict.get(char, 0)

        for char in ransomNote:
            if char not in magazine_dict or magazine_dict[char] == 0:
                return False
            else:
                magazine_dict[char] -= 1

        return True
