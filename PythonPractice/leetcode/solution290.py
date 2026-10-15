# Word Pattern
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s_list = s.split(" ")
        pattern_list = [char for char in pattern]

        if not self.is_surjective(pattern_list, s_list) or not self.is_injective(pattern_list, s_list):
            return False
        else:
            return True

    def is_surjective(self, pattern_list, s_list):
        return len(set(pattern_list)) == len(set(s_list)) and len(pattern_list) == len(s_list)

    def is_injective(self, pattern_list, s_list):
        hashmap = dict()
        for char, word in zip(pattern_list, s_list):
            if char not in hashmap:
                hashmap[char] = word
                continue

            if hashmap[char] != word:
                return False
        return True
